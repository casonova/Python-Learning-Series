from pokemon import Pokemon
from trainer import Trainer

# Create some Pokemon objects
pikachu = Pokemon("Pikachu", 100)
charmander = Pokemon("Charmander", 80)
squirtle = Pokemon("Squirtle", 120)

# Create a Trainer
ash = Trainer("Ash")

# Test cases for adding Pokemon
def test_add_pokemon():
    assert ash.add_pokemon(pikachu) == "Caught Pikachu with health 100"
    assert ash.add_pokemon(charmander) == "Caught Charmander with health 80"
    assert ash.add_pokemon(pikachu) == "This pokemon is already caught"
    assert ash.add_pokemon(squirtle) == "Caught Squirtle with health 120"

# Test cases for releasing Pokemon
def test_release_pokemon():
    assert ash.release_pokemon("Bulbasaur") == "Pokemon is not caught"
    assert ash.release_pokemon("Pikachu") == "You have released Pikachu"
    assert ash.release_pokemon("Charmander") == "You have released Charmander"
    assert ash.release_pokemon("Squirtle") == "You have released Squirtle"
    assert ash.release_pokemon("Pikachu") == "Pokemon is not caught"  # Pikachu was already released

# Test case for trainer data
def test_trainer_data():
    expected_output = "Pokemon Trainer Ash\n Pokemon count 0\n"
    assert ash.trainer_data() == expected_output

    ash.add_pokemon(squirtle)
    ash.add_pokemon(charmander)
    expected_output = "Pokemon Trainer Ash\n Pokemon count 2\n- Squirtle with health 120\n- Charmander with health 80\n"
    assert ash.trainer_data() == expected_output

# Run the test cases
test_add_pokemon()
test_release_pokemon()
test_trainer_data()

print("All test cases passed!")
