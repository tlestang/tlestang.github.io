(add-to-list 'load-path (expand-file-name "~/.emacs.d/elpa/htmlize-20191111.2130"))
(add-to-list 'load-path (expand-file-name "~/.emacs.d/elpa/org-20200803"))

(require 'htmlize)
(require 'ox)

(setq org-html-htmlize-output-type 'css)
(setq htmlize-output-type 'css)
