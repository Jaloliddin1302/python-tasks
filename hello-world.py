menu = ['osh', 'shashlik', 'manti', 'lagmon']
buyurtmalar = ['osh', 'shashlik', 'manti', 'somsa', 'norin']

for taom in buyurtmalar:
      if taom in menu:
          print(f'Menuda {taom} bor')
      else:
          print(f'Kechirasiz menuda {taom} yoq')