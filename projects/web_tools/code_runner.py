import sys
import io
import contextlib
import traceback

def execute_python_code(code_str):
    """
    Executes Python code string and captures stdout/stderr.
    WARNING: allow_exec=True implies security risk if exposed publicly.
    For a local student project, this is acceptable.
    """
    # Create a buffer to capture output
    output_buffer = io.StringIO()
    
    try:
        # Redirect stdout to our buffer
        with contextlib.redirect_stdout(output_buffer):
            # Create a shared dictionary for local variables to simulate a script scope
            local_scope = {}
            exec(code_str, {}, local_scope)
            
        return {"output": output_buffer.getvalue(), "status": "success"}
        
    except Exception:
        # Capture the full traceback if an error occurs
        return {"output": traceback.format_exc(), "status": "error"}
