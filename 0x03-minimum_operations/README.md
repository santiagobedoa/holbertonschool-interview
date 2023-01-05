# [Minimum Operations](https://intranet.hbtn.io/projects/488)

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
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using
    <code>
     python3
    </code>
    (version 3.4.3)
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    The first line of all your files should be exactly
    <code>
     #!/usr/bin/python3
    </code>
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    Your code should be documented
   </li>
   <li>
    Your code should use the
    <code>
     PEP 8
    </code>
    style (version 1.7.x)
   </li>
   <li>
    All your files must be executable
   </li>
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/488)

</html>

# Overwiew

To solve this problem, we can start by finding the largest power of 2 that is less than or equal to n, since we can always achieve any number that is a power of 2 using only Copy All and Paste operations. Then, we can repeatedly perform Paste operations to reach the desired number of H characters.