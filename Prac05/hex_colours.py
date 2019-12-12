colors = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Beige": "#f5f5dc", "Black": "#000000",
          "Blue1": "#0000ff", "Brown1": "#ff4040", "CadetBlue1": "#98f5ff", "chartreuse1": "#7fff00",
          "coral": "#ff7f50", "CornflowerBlue": "#6495ed"}
lower_colors = {key.lower(): value for key, value in colors.items()}
print(lower_colors)
color_name = input("Enter Color Name: ").lower()
while color_name != "":
        print("{}'s code is {}".format(color_name, lower_colors.get(color_name)))
        color_name = input("Enter Color Name: ").lower()

