katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        popup_alert = "The line is currently:"
        for i in range(len(katz_deli)):
            popup_alert = popup_alert + f' {i + 1}. {katz_deli[i]}'
        print(popup_alert)

  
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')
    
    
def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]   