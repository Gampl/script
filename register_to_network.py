import subprocess

def register_to_network():
    # Command to register to the network
    cmd = ["btcli", "s", "register", "--subtensor.network", "finney", "--netuid", "27"]

    try:
        # Execute the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True, input="root\nroot_hot\n", timeout=60)

        # Check if registration was successful
        if "Insufficient balance" in result.stdout:
            print("Insufficient balance. Retrying...")
            return False
        else:
            print("Registration successful!")
            return True
    except subprocess.TimeoutExpired:
        print("Registration process timed out. Retrying...")
        return False
    except Exception as e:
        print(f"Error: {e}. Retrying...")
        return False

def main():
    while True:
        success = register_to_network()
        if success:
            break

if __name__ == "__main__":
    main()
