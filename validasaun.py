import re        
import argparse 

print("====================================")
print("   Programa Validasaun Regex")
print("   Autor  : Maria mendosa")
print("====================================\n")

# =========================
# Regex patterns
# =========================
EMAIL_RE = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')  # Pattern ba validasaun email
PHONE_RE = re.compile(r'^\+?\d{7,15}$')               # Pattern geral ba telefone
PHONE_TL = re.compile(r'^(\+670|670)?7\d{6,7}$')      # Pattern telefone movel Timor-Leste

# =========================
# Funsaun valida email
# =========================
def valida_email(email: str) -> bool:
    # Retorna True se email mak passa regex, lae False se la passa
    return bool(EMAIL_RE.match(email.strip()))

# =========================
# Funsaun valida telefone
# =========================
def valida_phone(phone: str) -> bool:
    phone = re.sub(r'[\s\-\(\)]', '', phone)
    return bool(PHONE_RE.match(phone) or PHONE_TL.match(phone))

# =========================
# Modu interaktiv
# =========================
def interactive_mode():
    print("Modo interaktiv — valida email ou nomor telefone")
    while True:
        # Hili opsaun husi user
        choice = input("\nHili (e=email, p=phone, q=quit): ").lower()
        if choice == "q":
            print("Sai...")
            break
        if choice == "e":
            e = input("Hatama email: ")
            print("VALID" if valida_email(e) else "INVALID")
        elif choice == "p":
            p = input("Hatama telefone: ")
            print("VALID" if valida_phone(p) else "INVALID")

# =========================
# Funsaun prinsipál
# =========================
def main():
    parser = argparse.ArgumentParser(add_help=False)  # La uza help otomátiku
    parser.add_argument("--email")                     # Argumento ba email
    parser.add_argument("--phone")                     # Argumento ba phone
    parser.add_argument("--interactive", action="store_true")  # Mode interaktiv
    args, _ = parser.parse_known_args()

    # Se la iha argumento → direto simu interaktiv mode
    if not any([args.email, args.phone, args.interactive]):
        interactive_mode()
        return

    if args.interactive:
        interactive_mode()
    # Validasaun email se argumento email iha
    if args.email:
        print("Email:", "VALID" if valida_email(args.email) else "INVALID")
    # Validasaun telefone se argumento phone iha
    if args.phone:
        print("Phone:", "VALID" if valida_phone(args.phone) else "INVALID")

# =========================
# Entry point programa
# =========================
if __name__ == "__main__":
    main()
