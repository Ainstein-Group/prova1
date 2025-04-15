```markdown
#  Bandiera Italiana Assembly

Questo script assembly disegna la bandiera italiana in un terminale.

## Requisiti

*  Un assembler compatibile con NASM

##  Utilizzo

1. Salvate il codice come `flag.asm`.
2. Assemblate il codice usando il seguente comando:
   ```bash
   nasm -felf -o flag flag.asm
   ```
3. Eseguite il file eseguibile generato:
   ```bash
   ./flag 
   ```


## Descrizione

* Il codice definisce le dimensioni della bandiera in larghezza ed in altezza. 
* I caratteri utilizzati per rappresentare i colori della bandiera sono definiti.

```assembly
; Questo script assembly disegna la bandiera italiana in un terminale.
; 
; Definisci le dimensioni della bandiera
WIDTH     EQU 30     ; Larghezza della bandiera in caratteri
HEIGHT    EQU 20     ; Altezza della bandiera in caratteri
GREENCHAR EQU ' '     ; Carattere per il verde
WHCHAR EQU '*'    ; Carattere per il bianco
REDCHAR EQU '#'    ; Carattere per il rosso

; Disegna la bandiera 

green_section:
    mov esi, 0       ; Inizializza il registro ESI con 0
    mov edi, 0       ; Inizializza il registro EDI con 0
green_loop:   
    mov al, greenchar
    int 0x10        ; Stampa un carattere
    inc edi
    cmp edi,  WIDTH
    jl green_loop    ; Continua il loop se EDI è minore di WIDTH



    ; Disegna la seconda fascia bianca
white_section:
    mov esi, 0       ; Inizializza il registro ESI con 0
    mov edi, HEIGHT/3 ; Inizializza il registro EDI con l'altezza della terza fascia
white_loop:   
    mov al, whchar
    int 0x10        ; Stampa un carattere
    inc edi
    cmp edi, HEIGHT/3
    jl white_loop    ; Continua il loop se EDI è minore di HEIGHT/3

    ; Disegna la terza fascia rossa
red_section:

    mov esi, 0       ; Inizializza il registro ESI con 0
    mov edi, (HEIGHT/3)*2   ; Inizializza il registro EDI con l'altezza della terza fascia
red_loop:
    mov al, redchar
    int 0x10        ; Stampa un carattere

    inc edi
    cmp edi, HEIGHT
    jl red_loop    ; Continua il loop se EDI è minore di HEIGHT