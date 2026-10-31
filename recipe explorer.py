# ---- Recipe Explorer ----

# Step 1
pasta = ("Pasta Arrbiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

# step 2
all_recipes = (pasta, biryani)
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "mins")
print("Pasta details (sliced):",pasta[1:3])

#step 3
print("\nPasta Recipe details:")
for detail in pasta:
    print(" - ", detail)

#step 4
pasta_ingrediants = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingrediants = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingrediants:",pasta_ingrediants)
print("Biryani ingrdiants:", biryani_ingrediants)
print("Total pasta ingrediants:", len(pasta_ingrediants))

#stap 5
pasta_ingrediants.add("parmesan")
pasta_ingrediants.discard("chilli")
print("\nUpdated pasta ingredients:", pasta_ingrediants)

#step 6
all_ingrediants = pasta_ingrediants.union(biryani_ingrediants)
common = pasta_ingrediants.intersection(biryani_ingrediants)
only_pasta = pasta_ingrediants.difference(biryani_ingrediants)
unique_to_each = pasta_ingrediants.symmetric_difference(biryani_ingrediants)

print("\nAll ingrediants (union):",all_ingrediants)
print("Common ingredients (intersection):",common)
print("Only in pasta (difference):",only_pasta)
print("Not shared (sym.difference):", unique_to_each) 