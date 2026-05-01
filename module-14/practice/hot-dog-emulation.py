from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float
    min_stock: int = 5
    
    
@dataclass
class Recipe:
    name: str
    ingredient_keys: list[str]
    
class RecipeFactory:
    @staticmethod
    def get_standard_recipes() -> dict[int, Recipe]:
        return {
            1: Recipe("Хот-дог-1", ["bun", "sausage", "mustard", "ketchup"]),
            2: Recipe("Хот-дог-2", ["bun", "sausage", "jalapeno", "chili"]),
            3: Recipe("Хот-дог-3", ["bun", "sausage", "onion", "pickle", "mayonnaise"]),
            
        }

class HotDogBuilder:
    def __init__(self):
        self._ingredient_keys = ["bun", "sausage"]
        
    def add_ingredient(self, key: str):
        if key not in self._ingredient_keys:
            self._ingredient_keys.append(key)
        return self
    
    def build(self) -> Recipe:
        return Recipe("Свой хот-дог", self._ingredient_keys)
    
@dataclass
class OrderItem:
    recipe: Recipe
    quantity: int
    
    def total_price(self, ingredients: dict[str, Ingredient]) -> float:
        one_hotdog_price = sum(ingredients[key].price for key in self.recipe.ingredient_keys)
        return one_hotdog_price * self.quantity
    
    def total_cost(self, ingredients: dict[str, Ingredient]) -> float:
        one_hotdog_cost = sum(ingredients[key].cost for key in self.recipe.ingredient_keys)
        return one_hotdog_cost * self.quantity
    
@dataclass
class Order:
    items: list[OrderItem]
    payment_type: str
    
    def calculate_discount(self) -> float:
        total_quantity = sum(item.quantity for item in self.items)
        if total_quantity >= 5:
            return 0.15
        elif total_quantity >= 3:
            return 0.10
        else:
            return 0.0
        
    def total_price(self, ingredients: dict[str, Ingredient]) -> float:
        subtotal = sum(item.total_price(ingredients) for item in self.items)
        discount = self.calculate_discount()
        return subtotal * (1 - discount)
    
    def total_cost(self, ingredients: dict[str, Ingredient]) -> float:
        return sum(item.total_cost(ingredients) for item in self.items)
    
    def total_profit(self, ingredients: dict[str, Ingredient]) -> float:
        return self.total_price(ingredients) - self.total_cost(ingredients)
    
    def to_text(self, ingredients: dict[str, Ingredient]) -> str:
        lines = ["Информация о заказе:"]
        
        for item in self.items:
            ingredients_names = [ingredients[key].name for key in item.recipe.ingredient_keys]
            lines.append(f"Хот-дог: {item.recipe.name}")
            lines.append(f"Количество: {item.quantity}")
            lines.append("Состав:")

            for name in ingredients_names:
                lines.append(f"- {name}")
            
            lines.append(f" Цена позиции: {item.total_price(ingredients)} руб.")

        lines.append(f"Способ оплаты: {self.payment_type}")
        lines.append(f"Общая сумма: {self.total_price(ingredients):.2f} руб.")
        lines.append(f"Скидка: {self.calculate_discount() * 100:.0f}%")

        return "\n".join(lines)
    
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f" Оплата наличными выполнена на сумму {amount:.2f} руб."
    
class CardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f" Оплата картой выполнена на сумму {amount:.2f} руб."
    


class FileOrderSaver:
    def __init__(self, filename: str = "hotdog_orders.txt"):
        self.filename = filename

    def save(self, order: Order, ingredients: dict[str, Ingredient]):
        order_text = order.to_text(ingredients)
        
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(order_text)
                file.write("\n" + "-" * 50 + "\n")
            print(f"Заказ сохранен в файл: {self.filename}")
        except Exception as e:
            print(f"Ошибка при сохранении заказа: {e}")
            
def create_ingredients() -> dict[str, Ingredient]:
    return {
        "bun": Ingredient("Булочка", "bun", 0.5, 0.2),
        "sausage": Ingredient("Сосиска", "sausage", 1.0, 0.4),
        "mustard": Ingredient("Горчица", "mustard", 0.2, 0.05),
        "ketchup": Ingredient("Кетчуп", "ketchup", 0.2, 0.05),
        "mayonnaise": Ingredient("Майонез", "mayonnaise", 0.2, 0.05),
        "onion": Ingredient("Сладкий лук", "onion", 0.3, 0.1),
        "jalapeno": Ingredient("Халапеньо", "jalapeno", 0.4, 0.15),
        "chili": Ingredient("Чили", "chili", 0.35, 0.12),
        "pickle": Ingredient("Соленый огурец", "pickle", 0.25, 0.1),
    }

def create_stock() -> dict[str, int]:
    return {
        "bun": 50,
        "sausage": 40,
        "mustard": 30,
        "ketchup": 30,
        "mayonnaise":30,
        "onion": 20,
        "chili": 15,
        "pickle": 20,
        "jalapeno": 20,
         }
    
    
def get_toppings() -> list[str]:
    return [
        "mustard",
        "ketchup",
        "mayonnaise",
        "onion",
        "jalapeno",
        "chili",
        "pickle"
        
        ]
    
class Inventory:
    def __init__(self, ingredients: dict[str, Ingredient], stock: dict[str, int]):
        self.ingredients = ingredients
        self.stock = stock

    def has_enough(self, ingredient_keys: list[str], quantity: int) -> bool:
        for key in ingredient_keys:
            if self.stock.get(key, 0) < quantity:
                return False
        return True
    
    def reduce_stock(self, ingredient_keys: list[str], quantity: int):
        for key in ingredient_keys:
            if key in self.stock:
                self.stock[key] -= quantity
                
    def get_low_stock_items(self) -> list[Ingredient]:
        low_stock = []
        for key, ingredient in self.ingredients.items():
            if self.stock.get(key, 0) <= ingredient.min_stock:
                low_stock.append(ingredient)
        return low_stock
    
    def show(self):
        print("Наличие ингредиентов")
        low_stock_items = self.get_low_stock_items()
        
        for key, ingredient in self.ingredients.items():
            current_stock = self.stock.get(key, 0)
            status = "НИЗКИЙ ЗАПАС" if current_stock <= ingredient.min_stock else "В норме"
            print(f"{ingredient.name}: {current_stock} шт. ({status})")
            
        if low_stock_items:
            print("Необходимо пополнить запасы:")
            for item in low_stock_items:
                print(f" {item.name}(осталось: {self.stock[item.key]}шт., минимум: {item.min_stock})")
                
class SalesReport:
    def __init__(self):
        self.profit = 0.0
        self.revenue = 0.0
        self.sold_count = 0

    def add_order(self, order: Order, ingredients: dict[str, Ingredient]):
        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print("Отчет")
        print(f"Продано хот-догов: {self.sold_count}")
        print(f"Выручка: {self.revenue:.2f} руб.")
        print(f"Прибыль: {self.profit:.2f} руб.")
       

def show_menu():
    print("1. Создать заказ")
    print("2. Отчет")
    print("3. Наличие ингредиентов")
    print("4. Выход")
    

def show_standart_recipes(recipes: dict[int, Recipe], ingredients: dict[str, Ingredient]):
    print("Стандартные пиццы")

    for number, recipe in recipes.items():
        recipe_price = sum(ingredients[key].price for key in recipe.ingredient_keys)
        print(f"{number}. {recipe.name}")
        print(f"Состав: {', '.join([ingredients[key].name for key in recipe.ingredient_keys])}")
        print(f"Цена за штуку: {recipe_price:.2f} руб.\n")
    
    
def choose_recipe(
        recipes: dict[int, Recipe],
        ingredients: dict[str, Ingredient],
        inventory: Inventory
        
) -> Recipe:
    
    while True:
        choice = input("Выберите вариант: ")
        if choice == "0":
            return create_custom_recipe(inventory)
        elif choice in ["1", "2", "3"]:
            recipe = recipes[int(choice)]
            if not inventory.has_enough(recipe.ingredient_keys, 1):
                print("Недостаточно ингредиентов для этого рецепта")
                continue
            return recipe
        else:
            print("Неверный выбор! Попробуйте снова")
            
def create_custom_recipe(inventory: Inventory) -> Recipe:
    builder = HotDogBuilder()
    print("Создание своего хот-дога")
    toppings = get_toppings()
    available_toppings = {key: inventory.ingredients[key] for key in toppings}
    print("Доступные добавки:")
    for i, (key, ingredient) in enumerate (available_toppings.items(), 1):
        print(f"{i}.{ingredient.name} - {ingredient.price:.2f} руб.")
    while True:
        topping_choice = input("Введите номер добавки:")
        if topping_choice == "0":
            break
        try:
            index = int(topping_choice) - 1
            if 0 <= index < len(available_toppings):
                key = list(available_toppings.keys())[index]
                builder.add_ingredient(key)
                print(f"Добавлена: {available_toppings[key].name}")
            else:
                print("Неверный номер!")
        except ValueError:
            print("Введите число!")
    return builder.build()

def choose_payment() -> tuple[PaymentStrategy, str]:
    print("1 - Наличные")
    print("2 - Карта")
    while True:
        choice = input("Ваш выбор:")
        if choice == "1":
            return CashPayment(), "Наличные"
        elif choice == "2":
            return CardPayment(), "Карта"
        else:
            print("Выберите 1 или 2")
            
def create_order(
    ingredients: dict[str, Ingredient],
    inventory: Inventory,
    report: SalesReport,
    file_saver: FileOrderSaver
):
    recipes = RecipeFactory.get_standard_recipes()
    items: list[OrderItem] = []
    
    while True:
        show_standart_recipes(recipes, ingredients)
        recipe = choose_recipe(recipes, ingredients, inventory)
        while True:
            try:
                quantity = int(input(f"Введите количество хот-догов '{recipe.name}': "))
                if quantity <= 0:
                    print("Количество должно быть положительным!")
                    continue
                break
            except ValueError:
                print("Введите число!")
      
        if not inventory.has_enough(recipe.ingredient_keys, quantity):
            print("Недостаточно ингредиентов для заказа.")
            continue
        items.append(OrderItem(recipe, quantity))
        more = input("Добавить ещё один вид хот-дога? (да/нет): ").lower()
        if more != "да":
            break
    if not items:
        print("Заказ пуст.")
        return

    payment_strategy, payment_type = choose_payment()
    order = Order(items, payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys, item.quantity)
    amount = order.total_price(ingredients)
    print(payment_strategy.pay(amount))
    file_saver.save(order, ingredients)
    report.add_order(order, ingredients)
    
def main():
    ingredients = create_ingredients()
    stock = create_stock()

    inventory = Inventory(ingredients, stock)
    report = SalesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()

        choice = input("Выберите пункт меню: ")
        if choice == "1":
            create_order(ingredients, inventory, report, file_saver)
        elif choice == "2":
            report.show()
        elif choice == "3":
            inventory.show()
        elif choice == "4":
            break


if __name__ == "__main__":  
    main()

    
        
    
 
            
            
            
            
            





