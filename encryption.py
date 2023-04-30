class encryption(object):  
    def __init__(self, plaintext):
      self.plaintext = plaintext
      self.encryption_chars = "#;!ro4K7,l@|/z8QPu{9Wb[njqHV&>wLA$:etdxX2IGkSs3<=_0Y*?JmOic}pN6MfvE]1TZBR5y(h+C.)UD-F^g"
      self.ciphertext = ""
      self.encryption_chars_len = len(self.encryption_chars)

      
    def encrypt(self):
        for index in range(len(self.plaintext)):
            self.ciphertext += self.encryption_chars[(index + 10) % self.encryption_chars_len]
        return self.ciphertext
