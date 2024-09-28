

def convert_ounces_to_ml(oz):
    ml = oz * 29.57353
    # print(f'ml = {ml}')
    return ml

if __name__ == '__main__':
    print(float(convert_ounces_to_ml(5)))