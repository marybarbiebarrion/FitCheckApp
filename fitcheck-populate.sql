TRUNCATE TABLE "NutritionGuidance_allergen" CASCADE;
TRUNCATE TABLE "NutritionGuidance_ingredient" CASCADE;
TRUNCATE TABLE "NutritionGuidance_recipe" CASCADE;
TRUNCATE TABLE "NutritionGuidance_recipe_ingredients" CASCADE;
TRUNCATE TABLE "NutritionGuidance_meal" CASCADE;

---- Nutrition Guidance

-- Allergen

INSERT INTO "NutritionGuidance_allergen" (allergen_name) VALUES ('Milk');
INSERT INTO "NutritionGuidance_allergen" (allergen_name) VALUES ('Soy');
INSERT INTO "NutritionGuidance_allergen" (allergen_name) VALUES ('Tree Nuts');

-- Ingredient

INSERT INTO "NutritionGuidance_ingredient" (ingredient_name) VALUES ('Milk');
INSERT INTO "NutritionGuidance_ingredient" (ingredient_name) VALUES ('Ground Beef');
INSERT INTO "NutritionGuidance_ingredient" (ingredient_name) VALUES ('Cashew Nuts');
INSERT INTO "NutritionGuidance_ingredient" (ingredient_name) VALUES ('White Rice');

-- Recipe

INSERT INTO "NutritionGuidance_recipe" (recipe_instructions) VALUES ('i cooka da pizza');
INSERT INTO "NutritionGuidance_recipe" (recipe_instructions) VALUES ('i walk to burger king');
INSERT INTO "NutritionGuidance_recipe" (recipe_instructions) VALUES ('then i walk back home from burger king');
INSERT INTO "NutritionGuidance_recipe" (recipe_instructions) VALUES ('boo! gotcha didnt i?');

-- Recipe Ingredients

INSERT INTO "NutritionGuidance_recipe_ingredients" (quantity, ingredient_id_id, recipe_id_id) VALUES ('50 mL', (SELECT ingredient_id FROM "NutritionGuidance_ingredient" WHERE ingredient_name = 'Milk'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'i cooka da pizza'));
INSERT INTO "NutritionGuidance_recipe_ingredients" (quantity, ingredient_id_id, recipe_id_id) VALUES ('2 lbs', (SELECT ingredient_id FROM "NutritionGuidance_ingredient" WHERE ingredient_name = 'Ground Beef'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'i walk to burger king'));
INSERT INTO "NutritionGuidance_recipe_ingredients" (quantity, ingredient_id_id, recipe_id_id) VALUES ('3 pcs.', (SELECT ingredient_id FROM "NutritionGuidance_ingredient" WHERE ingredient_name = 'Cashew Nuts'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'then i walk back home from burger king'));
INSERT INTO "NutritionGuidance_recipe_ingredients" (quantity, ingredient_id_id, recipe_id_id) VALUES ('5 cups', (SELECT ingredient_id FROM "NutritionGuidance_ingredient" WHERE ingredient_name = 'White Rice'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'i walk to burger king'));
INSERT INTO "NutritionGuidance_recipe_ingredients" (quantity, ingredient_id_id, recipe_id_id) VALUES ('3 cups mL', (SELECT ingredient_id FROM "NutritionGuidance_ingredient" WHERE ingredient_name = 'White Rice'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));

-- Meal

INSERT INTO "NutritionGuidance_meal" (meal_name, calories, allergen_id_id, recipe_id_id) VALUES ('4 Cheese Pepperoni Pizza', 1000, (SELECT allergen_id FROM "NutritionGuidance_allergen" WHERE allergen_name = 'Milk'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'i cooka da pizza'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, allergen_id_id, recipe_id_id) VALUES ('Nutty Chocolate', 200, (SELECT allergen_id FROM "NutritionGuidance_allergen" WHERE allergen_name = 'Tree Nuts'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'then i walk back home from burger king'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, allergen_id_id, recipe_id_id) VALUES ('Korean Beef Bowl', 300, (SELECT allergen_id FROM "NutritionGuidance_allergen" WHERE allergen_name = 'Soy'), (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'i walk to burger king'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 1', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 2', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 3', 800, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 4', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 5', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 6', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 7', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 8', 1000, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 9', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 10', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 11', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 12', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 13', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 14', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 15', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 16', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 17', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 18', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 19', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 20', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 21', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 22', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));
INSERT INTO "NutritionGuidance_meal" (meal_name, calories, recipe_id_id) VALUES ('Filler Meal 23', 200, (SELECT recipe_id FROM "NutritionGuidance_recipe" WHERE recipe_instructions = 'boo! gotcha didnt i?'));









