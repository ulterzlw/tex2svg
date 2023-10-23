import subprocess

# Define the LaTeX document content as a string
latex_content = r"""
\documentclass[12pt, multi=sphinxmathenv, border=1pt]{standalone}

\begin{document}

\begin{sphinxmathenv}
  $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$
\end{sphinxmathenv}

\begin{sphinxmathenv}
  $E=mc^2$
\end{sphinxmathenv}

\begin{sphinxmathenv}
  $\boldmath{\mathcal{I}}_k = \left\{ \boldmath{a}_k, \boldmath{\omega}_k \right\}$
\end{sphinxmathenv}

\end{document}
"""

# Create a .tex file and write the LaTeX content to it
with open("mydocument.tex", "w") as tex_file:
    tex_file.write(latex_content)

# Run pdflatex to compile the .tex file to a PDF
subprocess.call(["pdflatex", "mydocument.tex"])

# Run pdf2svg
subprocess.call(["pdf2svg", "mydocument.pdf", "mydocument-%02d.svg", "all"])

# Clean up intermediate files (optional)
subprocess.call(["rm", "mydocument.aux", "mydocument.log", "mydocument.tex", "mydocument.pdf"])
