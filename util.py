notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

major_scale = {
    'C' : ['C','D','E','F','G','A','B'],
    'C#' : ['C#','D#','F','F#','G#','A#','C'],
    'D' : ['D','E','F#','G','A','B','C#'],
    'D#' : ['D#','F','G','G#','A#','C','D'],
    'E' : ['E','F#','G#','A','B','C#','D#'],
    'F' : ['F','G','A','A#','C','D','E'],
    'F#' : ['F#','G#','A#','B','C#','D#','F'],
    'G' : ['G','A','B','C','D','E','F#'],
    'G#' : ['G#','A#','C','C#','D#','F','G'],
    'A' : ['A','B','C#','D','E','F#','G#'],
    'A#' : ['A#','C','D','D#','F','G','A'],
    'B' : ['B','C#','D#','E','F#','G#','A#']
}

major_harmonic_field = {
    'C' : ['C','Dm','Em','F','G','Am','Bm(b5)'],
    'C#' : ['C#','D#m','Fm','F#','G#','A#m','Cm(b5)'],
    'D' : ['D','Em','F#m','G','A','Bm','C#m(b5)'],
    'D#' : ['D#','Fm','Gm','G#','A#','Cm','Dm(b5)'],
    'E' : ['E','F#m','G#m','A','B','C#m','D#m(b5)'],
    'F' : ['F','Gm','Am','A#','C','Dm','Em(b5)'],
    'F#' : ['F#','G#m','A#m','B','C#','D#m','Fm(b5)'],
    'G' : ['G','Am','Bm','C','D','Em','F#m(b5)'],
    'G#' : ['G#','A#m','Cm','C#','D#','Fm','Gm(b5)'],
    'A' : ['A','Bm','C#m','D','E','F#m','G#m(b5)'],
    'A#' : ['A#','Cm','Dm','D#','F','Gm','Am(b5)'],
    'B' : ['B','C#m','D#m','E','F#','G#m','A#m(b5)']
}

def harmonic_field_similarity(chords):
    global notes

    pitch = ''
    match = ''
    for note in notes:
        match_aux = [chord for chord in chords if chord in major_harmonic_field[note]]
        if len(match_aux) > len(match):
            pitch = note
            match = match_aux
    
    if set(match) == set(chords):
        return pitch
    else:
        chords =  chords - match
        secundary_pitch = ''
        secundary_match = ''
        for note in major_scale[pitch][1:]:
            match_aux = [chord for chord in chords if chord in major_harmonic_field[note]]
            if len(match_aux) > len(match):
                secundary_pitch = note
                secundary_match = match_aux