###############################################################################
# ZONE RESERVÉE AUX TESTS EN BAS DU PROGRAMME APRÈS LA CLASSE Transmission    #
###############################################################################

class Transmission:

	def __init__(self, trame):
		self.trame = trame
		self.id = None
		self.temperature = None
		self.humidite = None
		# Question 4. Il fallait ajouter le garde fou ci-dessous pour éviter de
		# déclencher des erreurs lors du décodage de trames invalides.
		if self.est_valide():
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
		# Question 4. Il ne faut pas oublier le cas particulier 100%
		# d'humidité !
		if self.trame[16:28] == '10100000':
			return 100
		else:
			dec = int(self.trame[16:28], 2)
			return (dec - 900) / 10

	def decoder_humidite(self):
		if self.trame[28:36] == '10100000':
			return 100
		else:
			bits_gauche = self.trame[28:32] # bits 28, 29, 30 et 31
			bits_droite =self.trame[32:36] # bits 32, 33, 34 et 35
			chiffre_dec_gauche_str = str(int(bits_gauche, 2))
			chiffre_dec_droite_str = str(int(bits_droite, 2))
			return int(chiffre_dec_gauche_str + chiffre_dec_droite_str)
		
	def est_valide(self):
		# Question 4. Il fallait ajouter le garde fou ci-dessous pour rejeter
		# les trames trop longues ou trop courtes (question 4).
		if len(self.trame) != 40:
			return False
		
		bits_controle = self.trame[36:40]
		blocs_bits = [
			self.trame[0:8], 
			self.trame[8:16],
			self.trame[16:28],
			self.trame[28:36]
		]
		
		for i in range(4):
			# On commence par déterminer la parité du bloc.
			nb_uns_du_bloc = 0
			for bit in blocs_bits[i]:
				nb_uns_du_bloc += int(bit) # piège: int !
			parite_bloc = nb_uns_du_bloc % 2
			# On vérifie ensuite que la parité du bloc est cohérente avec le
			# bit de contôle qui lui correspond.
			if parite_bloc != int(bits_controle[i]): # piège: int !
				return False
		return True

###############################################################################
# ZONE RESERVÉE AUX TESTS pour les questions 1. et 2.                         #
###############################################################################

# Question 1. 
def test_decodages():
	trame_exemple = '0010101011001000010010001100011000101101'
	trans_exemple = Transmission(trame_exemple)
	assert trans_exemple.decoder_temperature() == 26.4
	assert trans_exemple.decoder_humidite() == 62


# Question 2.
def test_est_valide():
	# trames pour les tests
	trame_valide =   '00101010'+'11001000'+'010010001100'+'01100010'+'1101'
	trame_non_val1 = '00101010'+'11001000'+'010010001100'+'01100010'+'0101'
	trame_non_val2 = '00101010'+'11001000'+'010010001100'+'01100010'+'1111'
	trame_non_val3 = '00101010'+'11001000'+'010010001100'+'01100010'+'0010'
	# Ajouter vos tests ci-dessous.
	trans_valide = Transmission(trame_valide)
	assert trans_valide.est_valide() == True
	for trame in (trame_non_val1, trame_non_val2, trame_non_val3):
		trans = Transmission(trame)
		assert trans.est_valide() == False


# Question 3.
"""
En regardant le fichier data.txt, on se rend compte que quelques trames sont
anormalement trop courte ou trop longue. Le dépassement d'incice déclenché est
donc lié aux trames trop courte. Il faut donc rejeter ces trames trop courtes
pour permettre l'exécution de l'affichage. Il est légitime de rejeter
également les trames trop longues. Même si elles ne déclenchent pas le
dépassement d'indice, des trames représentent des données erronées mal
transmises qu'il faut écarter.
"""

# Question 4. Voir les ajouts aux méthodes __init__ et est_valide.