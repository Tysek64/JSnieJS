def acronym(components):
    return ''.join([el[0] for el in components])

def median(numbers):
    return sorted(numbers)[len(numbers) // 2] if len(numbers) % 2 else sum(sorted(numbers)[len(numbers) // 2 - 1:len(numbers) // 2 + 1]) / 2

def pierwiastek(base, epsilon=0.1):
    def step(prev): this = prev - ((prev ** 2 - base) / (2 * prev)); return this if abs(this ** 2 - base) <= epsilon else step(this)
    return step(1)

def make_alpha_dict(text):
    return {letter.lower(): [word for word in text.split(' ') if letter.lower() in word.lower()] for letter in text if letter.isalnum() and letter.lower()}

def flatten(lista):
    return sum([flatten(element) if isinstance(element, (list, tuple)) else [element] for element in lista], [])

if __name__ == '__main__':
    print(acronym(['Polskie', 'Koleje', 'Panstwowe']))
    print(median([1,4,3,4,2,2]))
    print(pierwiastek(5, 0.0001))
    print(make_alpha_dict('According to all known laws of aviation, there is no way a bee should be able to fly.'))
    print(flatten([1, [2, 3], [(4, 5), 6]]))
