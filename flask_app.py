from flask import Flask, render_template, jsonify, request
from game.game import TicTacToe, RandomComputerPlayer
from game.hangman import Hangman
from quiz.data import get_quiz_data, check_score
from quiz.storage import save_result, get_all_results
import tracker.manager as tracker_mgr
import chat.manager as chat_mgr
import store.manager as store_mgr
import os
import threading
import sys
import subprocess
from crypto.manager import crypto_mgr
from weather.manager import weather_mgr
from cinema.manager import cinema_mgr
from professional.industry import industry_guide


app = Flask(__name__)


# Global game states
tictactoe_game = None
player_o = RandomComputerPlayer('O')
hangman_game = None

def init_tictactoe():
    global tictactoe_game
    tictactoe_game = TicTacToe()

def init_hangman():
    global hangman_game
    hangman_game = Hangman()

@app.route('/')
def home():
    return render_template('home.html')

# --- Tic Tac Toe Routes ---
@app.route('/tictactoe')
def tictactoe_page():
    if tictactoe_game is None:
        init_tictactoe()
    return render_template('tictactoe.html')

@app.route('/api/tictactoe/move', methods=['POST'])
def tictactoe_move():
    global tictactoe_game
    if tictactoe_game is None:
        init_tictactoe()

    data = request.json
    square = int(data['square'])
    
    # Check if game is already over
    if tictactoe_game.current_winner:
        return jsonify({'board': tictactoe_game.board, 'winner': tictactoe_game.current_winner})

    # Human Move (X)
    if not tictactoe_game.make_move(square, 'X'):
        return jsonify({'error': 'Invalid move', 'board': tictactoe_game.board}), 400

    if tictactoe_game.current_winner:
        return jsonify({'board': tictactoe_game.board, 'winner': 'X'})
    
    if not tictactoe_game.empty_squares():
        return jsonify({'board': tictactoe_game.board, 'winner': 'Tie'})

    # Computer Move (O)
    c_square = player_o.get_move(tictactoe_game)
    tictactoe_game.make_move(c_square, 'O')
    
    if tictactoe_game.current_winner:
        return jsonify({'board': tictactoe_game.board, 'winner': 'O'})

    if not tictactoe_game.empty_squares():
        return jsonify({'board': tictactoe_game.board, 'winner': 'Tie'})

    return jsonify({'board': tictactoe_game.board, 'winner': None})

@app.route('/api/tictactoe/reset', methods=['POST'])
def tictactoe_reset():
    init_tictactoe()
    return jsonify({'board': tictactoe_game.board, 'winner': None})

# --- Hangman Routes ---
@app.route('/hangman')
def hangman_page():
    if hangman_game is None:
        init_hangman()
    return render_template('hangman.html')

@app.route('/api/hangman/guess', methods=['POST'])
def hangman_guess():
    global hangman_game
    if hangman_game is None:
        init_hangman()
    
    data = request.json
    letter = data.get('letter')
    
    if not letter or len(letter) != 1:
        return jsonify({'error': 'Invalid input'}), 400

    hangman_game.guess(letter)
    return jsonify(hangman_game.get_info())

@app.route('/api/hangman/reset', methods=['POST'])
def hangman_reset():
    init_hangman()
    return jsonify(hangman_game.get_info())

@app.route('/api/hangman/status', methods=['GET'])
def hangman_status():
    global hangman_game
    if hangman_game is None:
        init_hangman()
    return jsonify(hangman_game.get_info())

# --- Desktop Launchers ---
# Since Snake and Hanoi are Pygame (Desktop), we can't embed them easily in HTML.
# We will add buttons to LAUNCH them on the server/desktop side.

@app.route('/launch/snake')
def launch_snake():
    # Run in a separate thread/process so it doesn't block Flask
    def run_game():
        subprocess.run([sys.executable, 'game/snake.py'])
    
    threading.Thread(target=run_game).start()
    return "Snake launched! Check your taskbar."

@app.route('/launch/hanoi')
def launch_hanoi():
    def run_game():
        subprocess.run([sys.executable, 'game/hanoi.py'])
    
    threading.Thread(target=run_game).start()
    return "Tower of Hanoi launched! Check your taskbar."

@app.route('/launch/flappy')
def launch_flappy():
    def run_game():
        subprocess.run([sys.executable, 'game/flappy.py'])
    
    threading.Thread(target=run_game).start()
    return "Flappy Bird launched! Check your taskbar."

@app.route('/launch/pong')
def launch_pong():
    def run_game():
        subprocess.run([sys.executable, 'game/pong.py'])
    
    threading.Thread(target=run_game).start()
    return "Ping Pong launched! Check your taskbar."

# --- Password Generator Routes ---
@app.route('/password')
def password_page():
    return render_template('password.html')

@app.route('/api/password/generate', methods=['POST'])
def generate_password_api():
    try:
        from game.autopw import generate_password
    except ImportError:
        # Fallback if file isn't found in game/
        # This handles the case if user only has it in templates/python student project/
        # But we made sure to copy it to game/autopw.py
        return jsonify({'error': 'Backend module not found'}), 500

    data = request.json
    length = data.get('length', 12)
    use_upper = data.get('use_upper', True)
    use_lower = data.get('use_lower', True)
    use_digits = data.get('use_digits', True)
    use_special = data.get('use_special', True)

    pwd = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    if pwd.startswith("Error"):
        return jsonify({'error': pwd}), 400
        
    return jsonify({'password': pwd})

# --- Bank System Routes ---
@app.route('/bank')
def bank_page():
    return render_template('bank.html')

@app.route('/api/bank/register', methods=['POST'])
def bank_register():
    # Import locally to avoid issues if module missing
    from bank.bms import bank
    data = request.json
    acc_num = bank.create_account(data.get('name'), data.get('pin'), data.get('initial', 0))
    return jsonify({'account_number': acc_num})

@app.route('/api/bank/login', methods=['POST'])
def bank_login():
    from bank.bms import bank
    data = request.json
    account = bank.authenticate(data.get('acc_num'), data.get('pin'))
    
    if account:
        return jsonify({'success': True, 'account_data': account})
    return jsonify({'error': 'Invalid Credentials'}), 401

@app.route('/api/bank/transact', methods=['POST'])
def bank_transact():
    from bank.bms import bank
    data = request.json
    acc_num = data.get('acc_num')
    trans_type = data.get('type')
    amount = float(data.get('amount'))

    if trans_type == 'deposit':
        success, res = bank.deposit(acc_num, amount)
    elif trans_type == 'withdraw':
        success, res = bank.withdraw(acc_num, amount)
    else:
        return jsonify({'error': 'Invalid transaction'}), 400

    if success:
        return jsonify({'success': True, 'new_balance': res})
    return jsonify({'error': res}), 400

@app.route('/api/bank/status/<acc_num>')
def bank_status(acc_num):
    from bank.bms import bank
    account = bank.get_account(acc_num)
    if account:
        return jsonify(account)
    return jsonify({'error': 'Not found'}), 404

# --- Quiz System Routes ---
@app.route('/quiz')
def quiz_login():
    return render_template('quiz_login.html')

@app.route('/quiz/start_session', methods=['POST'])
def quiz_start_session():
    name = request.form.get('name')
    roll = request.form.get('roll')
    # In a real app, we might store this in session
    return render_template('quiz_exam.html', name=name, roll=roll)

@app.route('/api/quiz/data')
def quiz_data_api():
    return jsonify(get_quiz_data())

@app.route('/api/quiz/submit', methods=['POST'])
def quiz_submit_api():
    data = request.json
    answers = data.get('answers', {})
    
    # Needs name and roll passed from frontend or session
    # For now we will rely on client sending it with answers or basic logic
    # In this simple implementation, let's grab it from the JSON too if we update the frontend
    # OR we can just save it as "Unknown" if not in session. 
    # To fix this properly, let's look for name/roll in the data packet.
    
    name = data.get('name', 'Unknown')
    roll = data.get('roll', 'N/A')
    
    score, details = check_score(answers)
    
    # Save to CSV
    save_result(name, roll, score, 50)
    
    return jsonify({
        'score': score, 
        'total': 50,
        'details': details
    })

@app.route('/quiz/results')
def quiz_results_page():
    # In a real app, protect this with an Admin Password
    results = get_all_results()
    # Sort by latest first
    results.reverse()
    return render_template('quiz_results.html', results=results)

# --- Expense Tracker Routes ---
@app.route('/tracker')
def tracker_page():
    return render_template('tracker.html')

@app.route('/api/tracker/add', methods=['POST'])
def tracker_add():
    data = request.json
    tracker_mgr.add_expense(data['category'], data['amount'], data.get('description', ''))
    return jsonify({'success': True})

@app.route('/api/tracker/data')
def tracker_data():
    expenses = tracker_mgr.get_expenses()
    summary = tracker_mgr.get_summary()
    return jsonify({'expenses': expenses, 'summary': summary})

# --- Chat Routes ---
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/api/chat/get')
def chat_get():
    return jsonify(chat_mgr.get_messages())

@app.route('/api/chat/send', methods=['POST'])
def chat_send():
    data = request.json
    chat_mgr.add_message(data['user'], data['text'])
    return jsonify({'success': True})

# --- Store Routes ---
@app.route('/store')
def store_page():
    return render_template('store.html')

@app.route('/api/store/products')
def store_products():
    return jsonify(store_mgr.get_products())

@app.route('/api/store/cart')
def store_cart():
    # In a real app we would use session['cart_id']
    return jsonify(store_mgr.get_cart_details())

@app.route('/api/store/cart/add', methods=['POST'])
def store_add_cart():
    data = request.json
    return jsonify(store_mgr.add_to_cart(data['id']))

@app.route('/api/store/cart/update', methods=['POST'])
def store_update_cart():
    data = request.json
    return jsonify(store_mgr.update_quantity(data['id'], data['change']))

@app.route('/api/store/cart/clear', methods=['POST'])
def store_clear_cart():
    # If called from invoice "Back to Home", we clear it then.
    return jsonify(store_mgr.clear_cart())

@app.route('/store/checkout')
def store_checkout():
    # Get cart details to render the invoice
    cart = store_mgr.get_cart_details()
    # In a real app we'd verify not empty and save order to DB here
    return render_template('invoice.html', cart=cart)

# --- Blockchain Simulation Routes ---
@app.route('/blockchain')
def blockchain_page():
    return render_template('blockchain.html')

@app.route('/blockchain/learn')
def blockchain_learn():
    return render_template('blockchain_learn.html')

@app.route('/portfolio')
def portfolio_page():
    return render_template('portfolio.html')

# --- AI/ML Smart Lab Routes ---
@app.route('/aiml/sentiment')
def sentiment_page():
    return render_template('sentiment.html')

@app.route('/api/aiml/sentiment', methods=['POST'])
def sentiment_api():
    from aiml.sentiment import analyzer
    data = request.json
    text = data.get('text', '')
    result = analyzer.analyze(text)
    return jsonify(result)

@app.route('/aiml/predictor')
def predictor_page():
    return render_template('predictor.html')

@app.route('/api/aiml/predict', methods=['POST'])
def predict_api():
    from aiml.predictor import predictor
    data = request.json
    scores = data.get('scores', [])
    result = predictor.predict(scores)
    return jsonify(result)

@app.route('/aiml/spam')
def spam_page():
    return render_template('spam_detector.html')

@app.route('/api/aiml/spam', methods=['POST'])
def spam_api():
    from aiml.spam_detector import detector
    data = request.json
    text = data.get('text', '')
    result = detector.analyze(text)
    return jsonify(result)

@app.route('/aiml/digit')
def digit_page():
    return render_template('digit_recognizer.html')

@app.route('/api/aiml/digit', methods=['POST'])
def digit_api():
    from aiml.digit_recognizer import nn_model
    data = request.json
    pixels = data.get('pixels', [])
    result = nn_model.predict(pixels)
    return jsonify(result)

@app.route('/aiml/house')
def house_page():
    return render_template('house_estimator.html')

@app.route('/api/aiml/house', methods=['POST'])
def house_api():
    from aiml.house_estimator import estimator
    data = request.json
    area = int(data.get('area', 1000))
    bed = int(data.get('bed', 2))
    loc = int(data.get('loc', 5))
    age = int(data.get('age', 5))
    result = estimator.estimate(area, bed, loc, age)
    return jsonify(result)

@app.route('/aiml/fraud')
def fraud_page():
    return render_template('fraud_detector.html')

@app.route('/api/aiml/fraud', methods=['POST'])
def fraud_api():
    from aiml.fraud_detector import detector
    data = request.json
    amount = float(data.get('amount', 0))
    location = data.get('location', 'Local')
    freq = int(data.get('freq', 1))
    
    # Simulate a user balance for the logic
    result = detector.analyze(amount, location, freq, 250000)
    return jsonify(result)

@app.route('/learn/<project_id>')
def learn_project(project_id):
    from aiml.roadmaps_data import roadmaps
    if project_id in roadmaps:
        data = roadmaps[project_id]
        return render_template('learn_project.html', 
                               title=data['title'], 
                               subtitle=data['subtitle'],
                               english_steps=data['english']['steps'],
                               hinglish_steps=data['hinglish']['steps'],
                               english_details=data['english'].get('details', ''),
                               hinglish_details=data['hinglish'].get('details', ''),
                               english_code=data['english'].get('code', ''),
                               hinglish_code=data['hinglish'].get('code', ''))
    return redirect('/')

@app.route('/api/blockchain/chain')
def get_chain():
    from blockchain.logic import blockchain_instance
    chain_data = []
    for block in blockchain_instance.chain:
        chain_data.append(block.__dict__)
    return jsonify({
        "length": len(chain_data),
        "chain": chain_data,
        "pending_count": len(blockchain_instance.unconfirmed_transactions)
    })

@app.route('/api/blockchain/transaction', methods=['POST'])
def add_transaction():
    from blockchain.logic import blockchain_instance
    data = request.json
    required_fields = ["sender", "receiver", "amount"]
    if not all(field in data for field in required_fields):
        return "Invalid transaction data", 400

    blockchain_instance.add_new_transaction(data)
    return "Success", 201

@app.route('/api/blockchain/mine', methods=['POST'])
def mine_chain():
    from blockchain.logic import blockchain_instance
    result = blockchain_instance.mine()
    if not result:
        return jsonify({"error": "No transactions to mine"}), 400
    return jsonify({"message": "Block mined", "index": result})

# --- CryptoPulse Routes ---
@app.route('/cryptopulse')
def cryptopulse_page():
    return render_template('cryptopulse.html')

@app.route('/api/crypto/market')
def crypto_market_api():
    return jsonify(crypto_mgr.get_market_data())

# --- SkyWatch AI Routes ---
@app.route('/skywatch')
def skywatch_page():
    return render_template('skywatch.html')

@app.route('/api/weather/cities')
def weather_cities_api():
    return jsonify(weather_mgr.get_all_cities())

@app.route('/api/weather/data')
def weather_data_api():
    city = request.args.get('city')
    return jsonify(weather_mgr.get_weather(city))

# --- CinemAura Routes ---
@app.route('/cinema')
def cinema_page():
    return render_template('cinema.html')

@app.route('/api/cinema/movies')
def cinema_movies_api():
    query = request.args.get('search', '')
    return jsonify(cinema_mgr.search(query))

@app.route('/api/cinema/recommend/<int:movie_id>')
def cinema_recommend_api(movie_id):
    return jsonify(cinema_mgr.get_recommendations(movie_id))

# --- Project Studio (Teacher Tool) ---
@app.route('/studio')
def studio_page():
    return render_template('project_studio.html')

@app.route('/backend_master')
def backend_master():
    from aiml.master_class_data import master_projects
    return render_template('backend_master.html', projects=master_projects)

@app.route('/health')
def health_page():
    return render_template('health.html')

@app.route('/industry')
def industry_mastery():
    return render_template('industry_mastery.html', standards=industry_guide.get_all_standards())


if __name__ == '__main__':
    init_tictactoe()
    init_hangman()
    app.run(debug=True, port=5000)
