###############################################################################
# ZONE RESERVÉE AUX TESTS EN BAS DU PROGRAMME APRÈS LA CLASSE Transmission    #
###############################################################################

class Transmission:

	def __init__(self, trame):
		self.trame = trame
		self.id = None
		self.temperature = None
		self.humidite = None
		self.decoder()
		
	def __repr__(self):
		"""Méthode spéciale pour l'affichage avec print."""
		return f"ID : {self.id} / Temp. : {self.temperature}°C / Hum. : {self.humidite}%"
		
	def decoder(self):
		self.id = self.decoder_id()
		self.temperature = self.decoder_temperature()
		self.humidite = self.decoder_humidite()
	
	def decoder_id(self):
		# Rappel. int(chaine, 2) : conversion chaine binaire -> entier décimal
		return int(self.trame[0:8], 2)
		
	def decoder_temperature(self):
		pass # à remplacer par votre code

	def decoder_humidite(self):
		pass # à remplacer par votre code
		
	def est_valide(self):
		return False


###############################################################################
# ZONE RESERVÉE AUX TESTS pour les questions 1. et 2.                         #
###############################################################################

# Question 1. 
def test_decodages():
	# Trame pour les tests
	trame_exemple = '0010101011001000010010001100011000101101'
	# Ajouter vos tests ci-dessous.
	pass # à remplacer par votre code


# Question 2.
def test_est_valide():
	# Trames pour les tests
	trame_valide =   '00101010'+'11001000'+'010010001100'+'01100010'+'1101'
	trame_non_val1 = '00101010'+'11001000'+'010010001100'+'01100010'+'0101'
	trame_non_val2 = '00101010'+'11001000'+'010010001100'+'01100010'+'1111'
	trame_non_val3 = '00101010'+'11001000'+'010010001100'+'01100010'+'0010'
	# Ajouter vos tests ci-dessous.
	pass # à remplacer par votre code