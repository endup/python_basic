
INTEGER, PLUS, EOF ,MINUS,MUL,DIV ='INTEGER','PLUS','EOF','MINUS','MUL','DIV'
 
class Token(object):
	def __init__(self, type, value):
		# token type: INTEGER, PLUS, or EOF
		self.type = type
		# token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
		self.value = value

	def __str__(self):
		"""String representation of the class instance.
		Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
		return 'Token({type}, {value})'.format(
			type=self.type,
			value=repr(self.value)
			)
			
	def __repr__(self):
		return self.__str__()
		
class Interpreter(object):
	def __init__(self, text):
        # 输入加法表达式 如3+6
		self.text = text
        # 表达式以str存放，pos是下标
		self.pos = 0
        # 当前的下标对应的数据
		self.current_token = None
	def error(self):
		raise Exception('Error parsing input')
		
	def get_next_token(self):
		text = self.text
		#当pos指向超出text长度后
		if self.pos > len(text) - 1:
			return Token(EOF, None)
		#目前pos指向的数据
		current_char = text[self.pos]
		#根据目前数据的不同执行不同操作
		while current_char == ' ':
			self.pos +=1
			current_char = text[self.pos]

		if current_char.isdigit():
			token = Token(INTEGER, int(current_char))
			self.pos += 1
			return token

		if current_char == '+':
			token = Token(PLUS, current_char)
			self.pos += 1
			return token

		if current_char == '-':
			token = Token(MINUS, current_char)
			self.pos += 1
			return token

		if current_char == '*':
			token = Token(MUL, current_char)
			self.pos += 1
			return token

		if current_char == '/':
			token = Token(DIV, current_char)
			self.pos += 1
			return token

		
		self.error()
		
	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()
			
	def expr(self):
		left=0
		right=0
		self.current_token = self.get_next_token()
		#左边的数字
		while self.current_token.type==INTEGER:
			left = self.current_token.value+left*10
			self.eat(INTEGER)
		#运算符号确定
		op = self.current_token
		if op.type == PLUS:
			self.eat(PLUS)
		elif op.type==MINUS:
			self.eat(MINUS)
		elif op.type==MUL:
			self.eat(MUL)
		else:
			self.eat(DIV)
			
		#右边的数字
		while self.current_token.type==INTEGER:
			right = self.current_token.value+right*10
			self.eat(INTEGER)

		if op.type==PLUS:
			result = left + right
		elif op.type==MINUS:
			result = left - right
		elif op.type==MUL:
			result = left * right
		else:
			result = left / right
		return result
 
def main():
	while True:
		text = input('calc> ')
			
		interpreter = Interpreter(text.strip())
		try:
			result = interpreter.expr()
			print(result)
		except:
			print('Error parsing input')
			pass
        
 
if __name__ == '__main__':
	main()