output_file = open('files/accounts.txt','w')

for _ in range(5):
   line = input()
   output_file.write(line + '\n')
output_file.close()