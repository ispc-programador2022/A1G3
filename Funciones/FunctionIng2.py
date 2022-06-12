class FunctionIng2:

    def ing2i(self):
        int_val = []
        for i in range(2):
            int_val.insert(i, int(input("Ingrese un valor numerico: ")))
        return int_val

    def ing2s(self):
        string_val = []
        for i in range(2):
            string_val.insert(i, input("Ingrese una cadena de carateres: "))
        return string_val
