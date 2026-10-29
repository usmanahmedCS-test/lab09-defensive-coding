import os
import sys

def calculate_risk_index_secure():
    user_input = input("Enter two metrics separated by a space: ")
    
    # DEFENSIVE FIX: Hard token breakdown and integer validation whitelisting
    try:
        tokens = user_input.split()
        if len(tokens) != 2:
            raise ValueError("Gateway requires exactly two metrics inputs.")
            
        metric_a = float(tokens[0])
        metric_b = float(tokens[1])
        
        # Explicit operations execution removes execution hazards completely
        print(f"Secure Risk Index: {metric_a * metric_b}")
        
    except ValueError as e:
        # DEFENSIVE FIX: Clean, non-verbose errors to deny system footprints
        print("Input Error: Invalid parameters submitted.")

def enforce_least_privilege():
    # DEFENSIVE FIX: Check identities and actively deny running under root accounts
    if hasattr(os, 'geteuid') and os.geteuid() == 0:
        print("[CRITICAL] Administrative root execution restricted for this component.")
        sys.exit(1)

if __name__ == "__main__":
    enforce_least_privilege()
    calculate_risk_index_secure()