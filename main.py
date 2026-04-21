from generator import PasswordGenerator

def main():
    print("--- 🛡️ Python OOP Password Generator ---")
    
    try:
        # User Inputs
        len_input = int(input("Enter password length: "))
        inc_upper = input("Include uppercase? (y/n): ").lower() == 'y'
        inc_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        inc_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Instantiate the Class
        pg = PasswordGenerator(
            length=len_input, 
            use_upper=inc_upper, 
            use_digits=inc_numbers, 
            use_special=inc_symbols
        )

        # Generate and Print
        password = pg.generate()
        print(f"\n✅ Generated Password: {password}")

    except ValueError as e:
        print(f"❌ Error: {e}. Please enter a valid number for length.")

if __name__ == "__main__":
    main()
