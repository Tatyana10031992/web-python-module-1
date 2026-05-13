# База данных

### `CREATE`

Создает объект: Таблица, база, индекс
```sql
CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  salary NUMERIC
)
```

### `TABLE`

Указывает, что создается или изменяется таблица
```sql
CREATE TABLE departaments(
  id SERIAL PRIMARY KEY,
  name TEXT,
)
```

### `ALTER`

Изменяет существубщий объект

```sql
ALTER TABLE employees
ADD COLUMN email TEXT
```

### `ADD`
Добавляет колонку, ограничения
```sql
ALTER TABLE employees
ADD COLUMN phone TEXT
```

### `DROP`
Удаляет объект (таблицу)
```sql
DROP TABLE projects;
```

### `IF EXISTS`
Позволяет избежать ошибки, если объекта нет
```sql
DROP TABLE IF EXISTS old_projects;
```

### `IF NOT EXISTS`
Создает объект только если он не существует
```sql
CREATE TABLE IF NOT EXISTS departaments (
id SERIAL PRIMARY KEY,
name TEXT
);
```

### `RENAME`
Переминовывет объекты
```sql
ALTER TABLE employees
RENAME COLUMN name to full_name;
```

### `TRUNCATE`
Быстро очищает таблицу
```sql
TRUNCATE TABLE projects;
```

## 2. Работа с данными
### `SELECT`
Выбирает данные
```sql
SELECT name, salary FROM employees;
```

### `FROM`
Указывает источник данных
```sql
SELECT name, salary FROM employees; 
```
### `INSERT`
Добавляет строки 
```sql
INSERT INTO departments(name)
VALUES ('id'), ('HR'), ('Finance');
```

### `INTO`
Указывает, куда вставлять данные
```sql
INSERT INTO employees(name, salary, demaptment_id)
VALUES ('Анна', 12000, 1);

```

### `VALUES`
Передвет конкретные значения
```sql
INSERT INTO projects(name, employee_id, budget)
VALUES ('CRM sYSTEM', 1, 500000);
```

