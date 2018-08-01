import csv

with open('gabes_data.csv', 'w', newline='') as f:
	fieldnames = ['PlayerName','ShoeColor','Address']
	thewriter = csv.DictWriter(f, fieldnames=fieldnames)

	thewriter.writeheader()
	for i in range(1,3):
		thewriter.writerow({'PlayerName':'Pete','ShoeColor':'Blue','Address':'Book'})
		thewriter.writerow({'PlayerName':'Von','ShoeColor':'Pie','Address':'Libros'})
		thewriter.writerow({'PlayerName':'Julio','ShoeColor':'Pie','Address':'Libros'})
		thewriter.writerow({'PlayerName':'George','ShoeColor':'Pie','Address':'Libros'})
		thewriter.writerow({'PlayerName':'Mark','ShoeColor':'Pie','Address':'Libros'})



#https://www.youtube.com/watch?v=royjxc1-R58&index=5&list=PL_rBtSh1CLjhxil_OXSXECqXI5mthbcNc
#https://www.youtube.com/watch?v=s1XiCh-mGCA