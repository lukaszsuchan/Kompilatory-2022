# Kompilatory-2022
Repozytorium do projektu w ramach przedmiotu 'Teoria Kompilacji i Kompilatory' na AGH z 2022 roku
| symbol |       token      |
|:------:|:----------------:|
| 🍎      | int              |
| 🍐      | long             |
| 🍇      | float            |
| 🍒      | double           |
| 🍓      | char             |
| 🍉      | string           |
| ❔      | boolean          |
| ⭐️      | void             |
| ⚡️      | null             |
| ✅      | true             |
| 🚫      | false            |
| ⏮      |assign            |
| ↪️      | for              |
| 🔁      | while            |
| ⏸      | if               |
| ⏯      | else             |
| 💡      | switch           |
| 🛄      | case             |
| 📬      | return           |
| 💥      | then             |
| ⛏      | do               |
| 🍞      | default          |
| 🍺      | break            |
| 📞      | call             |
| 🅰️      | and              |
| 🅾️      | or               |
| ❕      | not              |
| ➕      | plus             |
| ➖      | minus            |
| *️⃣      | times            |
| ➗      | devide           |
| 🌗      | equals           |
| 🌪       | not_equals       |
| 🌘      | greater          |
| 🌖      | lower            |
| 🌒      | greter_or_equal  |
| 🌔      | lower_or_equal   |
| 🌜      | l_parenthesis    |
| 🌛      | r_parenthesis    |
| 🤜      | l_square_bracket |
| 🤛      | r_square_bracket |
| 🔚      | end              |
| 🖨️      | print            |
| ⚙️      | function         |
|  [_a-zA-Z][_a-zA-Z0-9]*      | identifier       |
|   [0-9][.]+[0-9]*     | number_unsigned  |
|   \\"[_a-zA-Z0-9]*\\"     | text             |


* "Program" = "Blok"
<br>

* "Blok" = ["Blok_deklaracji"] 'end' ["Blok_instrukcji"] 'end'
<br>

* "Blok_deklaracji" = {"Dek_fun"} 
* "Dek_fun" = 'function' ("Var_sym" | 'void') 'identifier' 'l_parenthesis' {"Var_sym" 'identifier'} 'r_parenthesis' {"Instrukcja"} 'return' "Wyrazenie" 'end'
<br>

* "Blok_instrukcji" = {"Instrukcja"}
<br>

* "Instrukcja" = ("Instr_inicjuj" | "Instr_podstaw" | "Instr_wywolaj" | "Instr_if" | "Instr_while" | "Instr_for" | "Wypisz" | "Instr_switch") 'end'
<br>

* "Instr_inicjuj" = ("Var_liczba_sym" 'identifier' 'assign' ("Liczba" | 'null') | 'string' 'identifier' 'assign' ('text' | 'null'))
* "Instr_podstaw" = 'identifier' 'assign' ("Wyrazenie" | 'null')
* "Instr_wywolaj" = 'call' 'identifier' 'l_parenthesis' {"Wyrazenie"} 'r_parenthesis'
* "Instr_if" = 'if' "Warunek" 'then' "Instrukcja" {"Instrukcja"} ['end' 'else' "Instrukcja" {"Instrukcja"}]
* "Instr_while" = 'while' "Warunek" 'do' {"Instrukcja"}
* "Instr_for" = 'for' "For_warunek" 'do' {"Instrukcja"}
* "Wypisz" = 'print' ("Wyrazenie" | 'text')
* "Instr_switch" = 'switch' 'l_parenthesis' "Wyrazenie" 'r_parenthesis' "Case_blok" {"Case_blok"} "Case_default"
<br>
* "Case_blok" = 'case' 'l_parenthesis' "Wyrazenie" 'r_parenthesis' 'then' {"Instrukcja"} ['break'] 'end'
* "Case_default"  = 'default' 'then' {"Instrukcja"} 'end'
<br>

* "Var_sym" = ("Var_liczba_sym" | 'string' | 'boolean' | 'char')
* "Var_liczba_sym" = ('int' | 'long' | 'float' | 'double')
<br>

* "Wyrazenie" = ("Skladnik" {"Oper_add" "Skladnik"} | 'true' | 'false')
* "Skladnik" = "Czynnik" {"Oper_mul" "Czynnik"}
* "Oper_add" = ('plus' | 'minus')
* "Oper_mul" = ('times' | 'divide')
* "Czynnik" = ('identifier' | "Liczba" | "Instr_wywolaj" | "Wyr_w_naw")
* "Liczba" = ['minus'] 'number_unsigned'
* "Wyr_w_naw" = 'l_parenthesis' "Wyrazenie" 'r_parenthesis'
<br>

* "Warunek" = ['not'] "Warunek_prosty" {"Oper_war" "Warunek_prosty"}
* "Oper_war" = ('and' | 'or')
* "Warunek_prosty" = "Wyrazenie" ("Oper_porownania") "Wyrazenie"
* "Oper_porownania" = ('equals' | 'not_equals' | 'greater' | 'lower' | 'greter_or_equal' | 'lower_or_equal')
<br>

* "For_warunek" = ["Instr_inicjuj"] 'separator' ["Wyrazenie"] 'separator' ["Instr_podstaw"]
