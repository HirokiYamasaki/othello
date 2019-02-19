import random

WHITE = 0
BLACK = 1

class OhelloBorad (object):
	def __init__(self):
		self.cells = [[None for i in range(8)]for j in range(8)]
		self.cells[3][3] = BLACK
		self.cells[3][4] = WHITE
		self.cells[4][3] = WHITE
		self.cells[4][4] = BLACK
		#print(self.cells)
		
	def show_borad(self):
		print('=' * 45)
		print('    ',end='')
		for i in range(8):
			print(i,end='   ')
		print('\t')
		
		print(' ',end=' ')
		print('-' * 33)
		
		
		x = 0
		for i in self.cells:
			print(str(x) + ' |',end=' ')
			x += 1
			for j in i:
				if j == None:
					print('  ',end='')
				if j == 0:
					print('◯ ',end='')
				if j == 1:
					print('● ',end='')
					
				print('|',end=' ')
					
			print('\t')
			print('  ',end='')
			print('-' * 33)
			
	
	def flippable_disks(self,x,y,player):
		flippable = []
		DIR = [-1,0,1]
		
		for dx in DIR:
			for dy in DIR:
				if dx == 0 and dy == 0:
					continue
				
				tmp = []
				depth = 0
				while True:
					depth += 1
					rx = x + (dx * depth)
					ry = y + (dy * depth)
					
					if 0 <= rx < 8 and 0 <= ry < 8:
						request = self.cells[rx][ry]
					
						if request == None:
							break
						elif request == player:
							if tmp != []:
								flippable.extend(tmp)
								break
							else:
								break
						else:
							tmp.append((rx,ry))
								
					
					
					else:
						break
							
		return flippable
		
		
	def possible_disk(self,player):
		possible = []
		
		for i in range(8):
			for j in range(8):
				if self.cells[i][j] != None:
					continue
				
				if self.flippable_disks(i,j,player) == []:
					continue
				else:
					possible.append((i,j))
		
		return possible
		
		
	def human_put_disk(self,player):
		pos = self.possible_disk(player)
		print(pos)
		pos_len = int(len(pos))
	#	print(pos_len)
		
		print('    ',end='')
		for i in range(pos_len):
			print(i,end='       ')
		print('\n')
		
		if len(pos) == 0:
			print('パスです')
		else:
		
			while True:
				line = input('入力してください')
				if line.isdigit() == True:  	#数字が入力されている場合
					
					if int(line) < len(pos):		#数字がposの長さより小さい時
						break
					else:
						print('[エラー]上のリストのインデックスを入力してください')
							
				else:		#数字が入力されていない場合
					print('[エラー]数字を入力してください')
				
			LINE = int(line)
			
			print(pos[LINE][0],pos[LINE][1])
			
			self.cells[pos[LINE][0]][pos[LINE][1]] = player
			
			flippable = self.flippable_disks(pos[LINE][0],pos[LINE][1],player)
			print(flippable)
			
			for x,y in flippable:
				self.cells[x][y] = player
			
	
	def com_put_disk(self,player):
		pos = self.possible_disk(player)
		print(pos)
		print(len(pos))
		
		if len(pos) == 0:
			print('パスです')
		else:
			
			random_num = int(random.randint(0,(len(pos) - 1)))
			#print(random_num)
					
			#print(pos[random_num][0],pos[random_num][1])
			
			self.cells[pos[random_num][0]][pos[random_num][1]] = player
			
			flippable = self.flippable_disks(pos[random_num][0],pos[random_num][1],player)
			#print(flippable)
			
			for x,y in flippable:
				self.cells[x][y] = player
		
	
	def is_finish(self):
		flg = True
		pos_white = self.possible_disk(0)
		pos_black = self.possible_disk(1)
		
		if pos_white == [] and pos_black == []:
			flg = False
		
		return flg
				

	def result(self):
		siro = 0
		kuro = 0
		
		for x in range(8):
			for y in range(8):
				if self.cells[x][y] == WHITE:
					siro += 1
				elif self.cells[x][y] == BLACK:
					kuro += 1
		
		print('白' + str(siro) + '個')
		print('黒' + str(kuro) + '個')
		
		if siro < kuro:
			print('黒の勝ちです')
		elif siro > kuro:
			print('白の勝ちです')
		else:
			print('引き分け')
		
		
		
		
		


if __name__ == '__main__':
	borad = OhelloBorad()
	borad.show_borad()
	cnt = 0
	while True:
		cnt += 1
		if borad.is_finish() == False:
			break
		if int(cnt) % 2 == 0:
			print('白(com)の番です')
			player = 0
			borad.com_put_disk(player)
		elif int(cnt) % 2 == 1:
			print('黒(あなた)の番です')
			player = 1
			borad.human_put_disk(player)
			
		print('\n')
		borad.show_borad()
		
	#borad.show_borad()
	borad.result()
		