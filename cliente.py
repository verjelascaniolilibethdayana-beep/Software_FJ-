from entidad import Entidad


class Cliente(Entidad):
    """
    Representa a un cliente de Software FJ.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El correo electrónico no es válido.")

        correo_limpio = valor.strip()
        if correo_limpio.count("@") != 1 or " " in correo_limpio:
            raise ValueError("El correo electrónico no es válido.")

        usuario, dominio = correo_limpio.split("@")
        if not usuario or "." not in dominio:
            raise ValueError("El correo electrónico no es válido.")

        partes_dominio = dominio.split(".")
        if any(not parte for parte in partes_dominio):
            raise ValueError("El correo electrónico no es válido.")

        self._correo = correo_limpio
    
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (str, int)):
            raise ValueError("El teléfono debe tener al menos 7 dígitos.")

        telefono_str = str(valor).strip()
        if not telefono_str.isdigit() or len(telefono_str) < 7:
            raise ValueError("El teléfono debe tener al menos 7 dígitos.")

        self._telefono = telefono_str

    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
