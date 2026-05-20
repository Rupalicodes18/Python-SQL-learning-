import time
import random

def print_slow(text):
    """Creates a tense, hypnotic typing effect line by line."""
    for line in text.split('\n'):
        print(line)
        time.sleep(0.6)

def introduction():
    print_slow("""
    ==================================================
    PROJECT: LUCID HORIZON (SIMULATION ALPHA) 
    ==================================================
    You wake up with a sharp headache. Everything feels... artificial.
    The sky outside the window shifts from bright blue to a digital grey.
    A speaker on the wall crackles to life. 
    
    Voice: 'Subject's vitals stabilizing. Initiating memory reboot.'
    """)
    name = input("Enter your registered Subject Name: ")
    print(f"\nVoice: 'Welcome back, Subject {name}. Do not look at the cameras.'\n")
    return name

def access_terminal(hp, clarity, inventory):
    """Replaces the traditional medieval shop with a rogue mainframe terminal."""
    print_slow(f"""
    \n--- ROADSIDE ENCRYPTED TERMINAL ---
    You bypass a security terminal on the wall. It shows system diagnostics.
    Your Mental Clarity: {clarity}% | Neural HP: {hp}
    1. Inject Neuro-Stabilizer (+30 HP) -> Costs: 15 Clarity Points
    2. Download Decryption Key (Bypasses Security) -> Costs: 30 Clarity Points
    3. Log out of the terminal
    """)
    
    while True:
        action = input("Select command protocol (1, 2, or 3): ")
        if action == "1":
            if clarity >= 15:
                hp = min(100, hp + 30)
                clarity -= 15
                print(f"Neuro-Stabilizer injected! Neural HP: {hp} | Remaining Clarity: {clarity}%")
            else:
                print("ERROR: Insufficient Neural Clarity to process matrix rewrite!")
        elif action == "2":
            if clarity >= 30:
                clarity -= 30
                inventory.append("Decryption Key")
                print(f"Decryption Key saved to neural drive! Remaining Clarity: {clarity}%")
            else:
                print("ERROR: Mental energy too low to download corrupted data!")
        elif action == "3":
            print("\nTerminal connection severed. The shadows are watching.")
            break
    return hp, clarity, inventory

def meet_handler(hp, clarity, inventory):
    """The Logic Test — Inspired by Secret Societies and Illusion Loops."""
    print_slow("""
    \n--- THE CONSPIRACY ENCOUNTER ---
    You walk down a corridor and find a room lit only by candles. 
    A man sits in a velvet chair wearing a Venetian mask (Eyes Wide Shut vibe).
    It's the Handler.
    
    Handler: 'Everything you see is a carefully constructed lie. 
    If you want to wake up to reality, you must solve the fundamental paradox.'
    """)
    
    print("Question: 'I am a dream you can't wake up from, a truth you can't accept. The more I cover you, the less you know who you are. What am I?'")
    ans = input("Your Hypothesis: ").lower().strip()
    
    # Acceptable psychological answers: Illusion, Lie, Simulation, Mask
    if "illusion" in ans or "lie" in ans or "simulation" in ans or "mask" in ans:
        print_slow("\nHandler: 'Fascinating. You are starting to pierce through the veil.'")
        clarity += 50
        print("Mental Clarity restored! +50 Clarity Points. ")
    else:
        print_slow("\nHandler: 'Disappointing. You are deep within the rabbit hole.'")
        hp -= 25
        print("The simulation shocks your brain code! -25 Neural HP ")
        
    return hp, clarity, inventory

def start_game():
    player_name = introduction()
    hp = 70  
    clarity = 40  # Replaces Gold as currency
    inventory = ["ID Badge"]
    
    # Phase 1: Modifying the Reality Matrix
    hp, clarity, inventory = access_terminal(hp, clarity, inventory)
    
    # Phase 2: The Conspiracy Confrontation
    hp, clarity, inventory = meet_handler(hp, clarity, inventory)
    
    if hp <= 0:
        print("\n CRITICAL ERROR: Brain death occurred inside the simulation.")
        return

    # Phase 3: The Final Paradox Wall
    print_slow("""
    \n THE DEEP EXIT
    You reach the heavy steel doors of the facility. The alarm blares.
    The automated security system is wiping the mainframe! You have seconds left.
    """)
    print(f"Current Status -> Neural HP: {hp} | Drive Logs: {inventory}")
    
    ready = input("Do you attempt to breach the firewall code? (yes / no): ").lower().strip()
    if ready == "yes" or ready == "y":
        if "Decryption Key" in inventory:
            print_slow("\n SYSTEM PURGE INTERRUPTED! Your Decryption Key overrides the security matrix. The world shatters...")
            print_slow("You open your eyes. You are lying in a real bed. The sky outside is normal. You are free.")
        else:
            damage = random.randint(45, 65)
            hp -= damage
            print_slow(f"\n Without a key, you try to brute-force the mainframe. A massive feedback surge fry-cooks your brain! -{damage} HP.")
    else:
        print_slow("\nYou submit to the illusion. The simulation loops back to the beginning...")
        hp = 0

    # Ending Verification
    print("\n==================================================")
    if hp > 0:
        print_slow(f" PARADOX RESOLVED: Subject {player_name} has broken the cycle. Welcome back to the real world.")
        print(f"Final Integrity -> Neural HP: {hp} | Final Clarity: {clarity}%")
    else:
        print_slow(" REBOOTING... Subject trapped in eternal loops. Project: Lucid Horizon remains undefeated.")
    print("==================================================")

if __name__ == "__main__":
    start_game()
          
