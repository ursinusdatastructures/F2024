import numpy as np
import matplotlib.pyplot as plt
import subprocess

def backtrace(backpointers, node, involved):
    optimal = False
    for P in backpointers[node]:
        if backtrace(backpointers, (P[0], P[1]), involved):
            P[2] = True
            optimal = True
            involved[node[0], node[1]] = 1
    if node[0] == 0 and node[1] == 0:
        print(node)
        return True #Reached the beginning
    return optimal

def LevDist(a, b):
    #Third element in backpointers stores whether this is part
    #of an optimal path
    M = len(a)
    N = len(b)
    D = np.zeros((M+1, N+1))
    D[:, 0] = np.arange(M+1)
    D[0, :] = np.arange(N+1)
    backpointers = {}
    for i in range(0, M+1):
        for j in range(0, N+1):
            backpointers[(i, j)] = []
    for i in range(0, M):
        backpointers[(i+1, 0)].append([i, 0, False])
    for j in range(0, N):
        backpointers[(0, j+1)].append([0, j, False])
    for i in range(1, M+1):
        for j in range(1, N+1):
            delt = 1
            if a[i-1] == b[j-1]:
                delt = 0
            dul = delt + D[i-1, j-1]
            dl = 1 + D[i, j-1]
            du = 1 + D[i-1, j]
            D[i, j] = min(min(dul, dl), du)
            if dul == D[i, j]:
                backpointers[(i, j)].append([i-1, j-1, False])
            if dl == D[i, j]:
                backpointers[(i, j)].append([i, j-1, False])
            if du == D[i, j]:
                backpointers[(i, j)].append([i-1, j, False])
    involved = np.zeros((M+1, N+1))
    backtrace(backpointers, (M, N), involved) #Recursive backtrace from the end
    return (D, backpointers)


def writeChar(fout, i, j, c, bold = False):
    if bold:
        fout.write("\\node at (%g, %g) {\\textbf{%s}};\n"%(j+0.5, i+0.5, c))
    else:
        fout.write("\\node at (%g, %g) {%s};\n"%(j+0.5, i+0.5, c))

def drawPointers(fout, backpointers, M, N):
    for idx in backpointers:
        for P in backpointers[idx]:
            color = 'black'
            if P[2]:
                color = 'red'
            s = [idx[1]+1.4, M-idx[0]+0.8]
            if idx[0]-P[0] == 0: #Left arrow
                fout.write("\\draw [thick, ->, %s] (%g, %g) -- (%g, %g);\n"%(color, s[0], s[1], P[1]+1.6, s[1]))
            elif idx[1]-P[1] == 0: #Up arrow
                fout.write("\\draw [thick, ->, %s] (%g, %g) -- (%g, %g);\n"%(color, s[0], s[1], s[0], M-P[0]+0.2))
            else: #Diagonal Arrow
                fout.write("\\draw [thick, ->, %s] (%g, %g) -- (%g, %g);\n"%(color, s[0], s[1], P[1]+1.6, M-P[0]+0.2))

def drawAllPointers(fout, M, N):
    for i in range(1, M+1):
        for j in range(1, N+1):
            color = 'black'
            s = [j+1.4, M-i+0.8]
            #Left arrow
            fout.write("\\draw [thick, ->, %s] (%g, %g) -- (%g, %g);\n"%(color, s[0], s[1], j-1+1.6, s[1]))
            #Up arrow
            fout.write("\\draw [thick, ->, %s] (%g, %g) -- (%g, %g);\n"%(color, s[0], s[1], s[0], M-(i-1)+0.2))
            #Diagonal Arrow
            fout.write("\\draw [thick, ->, %s] (%g, %g) -- (%g, %g);\n"%(color, s[0], s[1], j-1+1.6, M-(i-1)+0.2))


def LevenshteinExample(a, b, doPointers = False, doAllPointers = False):
    #Make Levenshtein Example
    M = len(a)
    N = len(b)
    (D, backpointers) = LevDist(a, b)
    fout = open("levfig.tex", "w")
    fout.write("\\documentclass[12pt,oneside,a4paper]{article}")
    fout.write("\\usepackage{tikz}")
    fout.write("\\begin{document}")
    fout.write("\\begin{tikzpicture}")
    fout.write("\\draw [help lines] (0, 0) grid (%i,%i);\n"%(N+2, M+2))
    
    writeChar(fout, M, 0, '\\_')
    for i in range(M):
        writeChar(fout, M-(i+1), 0, a[i])
        
    writeChar(fout, M+1, 1, '\\_')
    for j in range(N):
        writeChar(fout, M+1, j+2, b[j])
    
    for i in range(M+1):
        for j in range(N+1):
            if i == M and j == N:
                continue
            writeChar(fout, M-i, j+1, int(D[i, j]))
    writeChar(fout, 0, N+1, int(D[-1, -1]))
    
    if doPointers:
        drawPointers(fout, backpointers, M, N)
    elif doAllPointers:
        drawAllPointers(fout, M, N)
    fout.write("\\end{tikzpicture}")
    fout.write("\\end{document}")
    fout.close()

    subprocess.call(["pdflatex", "levfig.tex"])


if __name__ == '__main__':
    LevenshteinExample("school", "fools", doPointers=False)
    #s = "razmataz"
    #s2 = s[::-1]
    #LevenshteinExample(s, s2, doPointers=True)
