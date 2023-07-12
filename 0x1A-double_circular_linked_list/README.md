# [Double Circular Linked List](https://intranet.hbtn.io/projects/478)

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Requirements
  </h2>
  <h3>
   General
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files will be compiled on Ubuntu 14.04 LTS
   </li>
   <li>
    Your programs and functions will be compiled with
    <code>
     gcc 4.8.4
    </code>
    using the flags
    <code>
     -Wall
    </code>
    <code>
     -Werror
    </code>
    <code>
     -Wextra
    </code>
    and
    <code>
     -pedantic
    </code>
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project is mandatory
   </li>
   <li>
    Your code should use the
    <code>
     Betty
    </code>
    style. It will be checked using
    <a href="https://github.com/hs-hq/Betty/blob/master/betty-style.pl" target="_blank" title="betty-style.pl">
     betty-style.pl
    </a>
    and
    <a href="https://github.com/hs-hq/Betty/blob/master/betty-doc.pl" target="_blank" title="betty-doc.pl">
     betty-doc.pl
    </a>
   </li>
   <li>
    You are not allowed to use global variables
   </li>
   <li>
    No more than 5 functions per file
   </li>
   <li>
    The only C standard library functions allowed are
    <code>
     malloc
    </code>
    ,
    <code>
     free
    </code>
    , and
    <code>
     strdup
    </code>
    . Any use of functions like
    <code>
     printf
    </code>
    ,
    <code>
     puts
    </code>
    ,
    <code>
     calloc
    </code>
    ,
    <code>
     realloc
    </code>
    etc… is forbidden
   </li>
   <li>
    In the following examples, the
    <code>
     main.c
    </code>
    files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own
    <code>
     main.c
    </code>
    files at compilation. Our
    <code>
     main.c
    </code>
    files might be different from the one shown in the examples
   </li>
   <li>
    The prototypes of all your functions should be included in your header file called
    <code>
     list.h
    </code>
   </li>
   <li>
    Don’t forget to push your header file
   </li>
   <li>
    All your header files should be include guarded
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <p>
   Please use this data structure for this project:
  </p>
  <pre><code>/**
 * struct List - doubly linked list
 * @str: string - (malloc'ed string)
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 * for Holberton project
 */
typedef struct List
{
  char *str;
  struct List *prev;
  struct List *next;
} List;
</code></pre>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/478)
</html>