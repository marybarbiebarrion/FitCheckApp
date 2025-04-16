DROP TABLE HYDRATION_TRACKER;
DROP TABLE MEAL_FAVORITES;
DROP TABLE MEAL;
DROP TABLE RECIPE_INGREDIENTS;
DROP TABLE RECIPE;
DROP TABLE INGREDIENT;
DROP TABLE USER_EMCONTACT;
DROP TABLE EMERGENCY_CONTACT;
DROP TABLE USER_INFO;
DROP DATABASE fitcheck_db;
CREATE DATABASE fitcheck_db;
GRANT ALL PRIVILEGES ON DATABASE fitcheck_db TO postgres;
\c fitcheck_db

-- User Profile

CREATE TABLE USER_INFO(
    user_id                     SERIAL NOT NULL UNIQUE PRIMARY KEY,
    email_address               VARCHAR(255) NOT NULL,
    password                    VARCHAR(255) NOT NULL,
    sex_at_birth                VARCHAR(255) NOT NULL,
    expression_of_consent       BOOLEAN NOT NULL,
    declaration_of_undertaking  BOOLEAN NOT NULL, 
    last_updated                DATE DEFAULT current_date NOT NULL, 
    first_name                  VARCHAR(255) NOT NULL,
    middle_name                 VARCHAR(255) NOT NULL, 
    last_name                   VARCHAR(255) NOT NULL, 
    suffix                      VARCHAR(255) NOT NULL, 
    nickname                    VARCHAR(255) NOT NULL, 
    birthdate                   DATE NOT NULL, 
    mobile_number               INT NOT NULL,
    barangay                    VARCHAR(255) NOT NULL, 
    city                        VARCHAR(255) NOT NULL, 
    region                      VARCHAR(255) NOT NULL, 
    province                    VARCHAR(255) NOT NULL, 
    country                     VARCHAR(255) NOT NULL, 
    initial_height              FLOAT(2) NOT NULL, 
    current_height              FLOAT(2) NOT NULL, 
    initial_weight              FLOAT(2) NOT NULL, 
    current_weight              FLOAT(2) NOT NULL 
);

CREATE TABLE EMERGENCY_CONTACT(
    contact_id         SERIAL NOT NULL UNIQUE PRIMARY KEY,
    contact_name       VARCHAR(255) NOT NULL,
    contact_email      VARCHAR(255) NOT NULL,
    contact_number     INT NOT NULL
);

CREATE TABLE USER_EMCONTACT(
    user_id     INT NOT NULL,
    contact_id  INT NOT NULL,
    is_primary  BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES USER_INFO(user_id) ON DELETE CASCADE,
    FOREIGN KEY (contact_id) REFERENCES EMERGENCY_CONTACT(contact_id) ON DELETE CASCADE
);

-- Food Analysis
CREATE TABLE INGREDIENT(
    ingredient_id   SERIAL NOT NULL UNIQUE PRIMARY KEY,
    ingredient_name VARCHAR(255) NOT NULL
);

-- Nutrition Guidance

CREATE TABLE RECIPE(
    recipe_id           SERIAL NOT NULL UNIQUE PRIMARY KEY,
    recipe_instructions TEXT NOT NULL
);

CREATE TABLE RECIPE_INGREDIENTS(
    recipe_id       INT NOT NULL,
    ingredient_id   INT NOT NULL,
    quantity        FLOAT(2) NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES RECIPE(recipe_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES INGREDIENT(ingredient_id) ON DELETE CASCADE
);

CREATE TABLE MEAL(
    meal_id     SERIAL NOT NULL UNIQUE PRIMARY KEY,
    meal_name   VARCHAR(255) NOT NULL,
    recipe_id   INT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES RECIPE(recipe_id) ON DELETE SET NULL
);

CREATE TABLE MEAL_FAVORITES(
    user_id         INT NOT NULL,
    meal_id         INT NOT NULL,
    is_calories     BOOLEAN NOT NULL DEFAULT FALSE,
    is_ingredients  BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES USER_INFO(user_id) ON DELETE CASCADE,
    FOREIGN KEY (meal_id) REFERENCES MEAL(meal_id) ON DELETE CASCADE
);

CREATE TABLE HYDRATION_TRACKER(
    user_id         INT NOT NULL,
    container_size  INT NOT NULL,
    water_goal      INT NOT NULL,
    active_hours    INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER_INFO(user_id) ON DELETE CASCADE
);