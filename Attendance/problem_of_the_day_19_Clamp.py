#Name: Khem Niraula
#Student ID: 0644115
#Due Date: Octobar 29, 2019
#MSITM 6341

def clamp(value, min, max):
    if value <=max and value >=min:
        return value
    elif value<min:
        return min
    elif value>min:
        return max

print(clamp(1,10,20))