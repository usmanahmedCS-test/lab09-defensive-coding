import os

def calculate_risk_index():
    # CRITICAL FLAW: eval() parses strings directly as live application commands.
    # Submitting "__import__('os').system('cat /etc/passwd')" executes unchecked RCE.
    user_input = input("Enter financial risk expression (e.g., 5 * 0.12): ")
    print(f"Risk Index Calculation Result: {eval(user_input)}")

if __name__ == "__main__":
    calculate_risk_index()