class MyChicken:

    def canFly(self):
        print('Chicken can fly')

    def canSwim(self):
        print('Chicken can swim')

class MyPenguin:
    def canFly(self):
        print('Penguin can\'t fly')

    def canSwim(self):
        print('Penguin can swim')

# Common interface
def flying_bird_test(bird):
    bird.canFly()
    bird.canSwim()

#