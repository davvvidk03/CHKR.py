# Decision Table — Recipe CLI

| Condition / Input                     | Valid Values                        | Action                                      |
|--------------------------------------|--------------------------------------|---------------------------------------------|
| Number of ingredients entered         | 3 or more                            | Generate meal suggestions using API         |
| Number of ingredients entered         | Less than 3                          | Return safe default: "Go grocery shopping." |
| Dietary restriction provided          | diabetes / vegan / halal / none      | Filter suggestions based on restriction     |
| Flavor profile preference             | asian / mediterranean / southern / no| Adjust recipe type accordingly              |
| **DEFAULT**                           | —                                    | Show help message or safe fallback          |
