
class Mycharm:
    def execute(self):
        print("Running")

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()  # or Mycharm() , it does not matter, only it matters is ,it should have execute() in it.

lap = laptop()
lap.code(ide)