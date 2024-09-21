import pandas as pd
# a = [1,7,2]
# myvar =pd.Series(a)
# print(myvar)
# cata =pd.Series([1,2,3,4,5])
# print(cata)
import pandas
data = {
    'cates':['1','2','3','4'],
    'chdyt':["Das","Acs","Esc","Ewa"]
}
myvar = pandas.DataFrame(data)
print(myvar)
# try:
#      df = pd.read_csv('Data.csv')
#      print(df.to_string())
# except:
#     print("File not found")
