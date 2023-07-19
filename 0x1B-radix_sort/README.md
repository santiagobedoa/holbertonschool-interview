# [Radix Sort](https://intranet.hbtn.io/projects/480)

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
    file, at the root of the folder of the project, is mandatory
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
    Unless specified otherwise, you are not allowed to use the standard library. Any use of functions like
    <em>
     printf, puts, …
    </em>
    is totally forbidden.
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
     sort.h
    </code>
   </li>
   <li>
    Don’t forget to push your header file
   </li>
   <li>
    All your header files should be include guarded
   </li>
   <li>
    A list/array does not need to be sorted if its size is less than 2.
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <p>
   For this project you are given the following
   <code>
    print_array
   </code>
   function:
  </p>
  <pre><code>alexa@ubuntu-xenial:0x1B-radix_sort$ cat `print_array.c`
#include &lt;stdlib.h&gt;
#include &lt;stdio.h&gt;

/**
 * print_array - Prints an array of integers
 *
 * @array: The array to be printed
 * @size: Number of elements in @array
 */
void print_array(const int *array, size_t size)
{
    size_t i;

    i = 0;
    while (array &amp;&amp; i &lt; size)
    {
        if (i &gt; 0)
            printf(", ");
        printf("%d", array[i]);
        ++i;
    }
    printf("\n");
}
alexa@ubuntu-xenial:0x1B-radix_sort$
</code></pre>
  <ul>
   <li>
    Our file
    <code>
     print_array.c
    </code>
    will be compiled with your function during the correction.
   </li>
   <li>
    Please declare the prototype of the function
    <code>
     print_array
    </code>
    in your
    <code>
     sort.h
    </code>
    header file
   </li>
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/480)
</html>