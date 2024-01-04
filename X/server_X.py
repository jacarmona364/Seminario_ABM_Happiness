from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import pandas as pd

class MyAgent(Agent):
    def __init__(self, unique_id, model, happiness, color):
        super().__init__(unique_id, model)
        self.happiness = happiness
        self.color = color

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()

class MyModel(Model):
    def __init__(self, N, width, height, excel_file_path):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Leer la primera columna desde el archivo Excel sin título
        df = pd.read_excel(excel_file_path, header=None)
        happiness_values = df.iloc[:, 0].tolist()

        # Mapeo de valores a colores
        color_mapping = {
            0: "Red",
            1: "Orange",
            2: "Yellow",
            3: "Green",
            4: "LightBlue",
            5: "DarkBlue"
        }

        for i in range(self.num_agents):
            happiness = happiness_values[i % len(happiness_values)]  # Ciclo por los valores si hay menos agentes que valores
            color = color_mapping.get(happiness, "Grey")  # Valor predeterminado "Grey" si no hay coincidencia
            a = MyAgent(i, self, happiness, color)
            self.schedule.add(a)
            # Asignar ubicación aleatoria en la cuadrícula
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            agent_reporters={"Pos": "pos"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()


# Definir el entorno gráfico
def agent_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "circle", "r": 0.7, "Filled": "true", "Layer": 0, "Color": agent.color}

    return portrayal

# Ruta del archivo Excel con las columnas 'Happiness' y 'Color'
excel_file_path = "C:/Users/pepec/Desktop/4ºGIIADE/Seminario_ABM_Happiness/X/model_X.xlsx"

# Tamaño de la cuadrícula (ajustar según sea necesario)
grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

# Crear el servidor de visualización
server = ModularServer(
    MyModel,
    [grid],
    "Modelo de Agentes",
    {"N": 371, "width": 50, "height": 50, "excel_file_path": excel_file_path}
)

server.port = 8521  # Configurar el puerto
server.launch()  # Lanzar el servidor
