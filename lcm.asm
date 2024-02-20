section .data
    seed dd 42
    a dd 1664525
    c dd 1013904223
    m dd 4294967296 

section .text
    global _start

_start:
    mov eax, [seed]

    mov ebx, [a]
    imul ebx
    mov ecx, [c]
    add eax, ecx
    mov edx, [m]
    xor ecx, ecx
    div edx
    mov [seed], eax

    mov eax, 1
    xor ebx, ebx
    int 0x80
