def decrypt_caesar_cipher(ciphertext):
    for shift in range(1, 26):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            else:
                decrypted_text += char
        print(f"Desplazamiento {shift}: {decrypted_text}")

# Aqui se ingreso el texto cifrado
ciphertext = "NOYZUXEOYVATIZAGZKJCOZNIUJKYZNKENGBKJKIOJKJZNKUAZIUSKYULHGZZRKYGTJRKJZUZNKJKGZNYULQOTMYGTJWAKKTYONGBKZNKXKLUXKHKKTGHRKZUIGRRAVUTYZUXOKYULVUROZOIGROTZXOMAKGTJZGRKYULROLKGTJJKGZNZUORRAYZXGZKZNKQKEZAXTOTMVUOTZYOTZNKKBURAZOUTGXEJKBKRUVSKTZULIUJKYZNKNOYZUXEULIUJKYOYYUOTUXJOTGZKREXOINZNGZONGBKHKKTLUXIKJZURKGBKUAZSGTELGYIOTGZOTMYZUXOKYCNOINOTZAXTSKGTYZNGZSEGIIUATZOYTUZJKLOTOZOBKOLEUACUARJROQKZULOTJUAZSUXKGHUAZEUAXLGBUXOZKZGRKUXEUAXLGBUXOZKIUJKHXKGQKXZNKTOCUARJXKLKXEUAZUZNKROYZULLAXZNKXXKGJOTMCNOINYNUARJNKRVZNUYKXKGJKXYCNUCUARJROQKZUYZAJEZNKYAHPKIZOTSUXKJKZGOR"  # Texto cifrado

decrypt_caesar_cipher(ciphertext)
