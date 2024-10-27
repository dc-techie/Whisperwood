class Art:

    title_art = r"""
    
█     █░ ██░ ██  ██▓  ██████  ██▓███  ▓█████  ██▀███   █     █░ ▒█████   ▒█████  ▓█████▄ 
▓█░ █ ░█░▓██░ ██▒▓██▒▒██    ▒ ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▓█░ █ ░█░▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
▒█░ █ ░█ ▒██▀▀██░▒██▒░ ▓██▄   ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒▒█░ █ ░█ ▒██░  ██▒▒██░  ██▒░██   █▌
░█░ █ ░█ ░▓█ ░██ ░██░  ▒   ██▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░█░ █ ░█ ▒██   ██░▒██   ██░░██▄  █▌
░░██▒██▓ ░▓█▒░██▓░██░▒██████▒▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒░░██▒██▓ ░ ████▓▒░░ ████▓▒░░█████▓ 
░ ▓░▒ ▒   ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ 
  ▒ ░ ░   ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░  ▒ ░ ░    ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ 
  ░   ░   ░  ░░ ░ ▒ ░░  ░  ░  ░░          ░     ░░   ░   ░   ░  ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ 
    ░     ░  ░  ░ ░        ░              ░  ░   ░         ░        ░ ░      ░ ░     ░    
                                                                                   ░     
"""

    @classmethod
    def get_title_art(cls):
        return cls.title_art.split('\n')

    side_tree_art = r"""
        *           
        /|      |\    
     *__\\ /\   //__* 
   /|    | \\  ||     
*__\\    `\ \\ |'__/ _
   ||  _* // \\|  _ / 
 \__*\ |  || //| /    
   *_\\ \ ||/ |//     
      \\   /  //      
       |     //       
       |     |        
       |     |        
       |     |        
    __/       \__     
"""

    @classmethod
    def get_side_tree_art(cls):
        return cls.side_tree_art.split('\n')

    merchant_art_good = r"""
     ___      
  __[___]__   
 (  _   _  )  
 |  o   o  |  
 |         |  
 |    C    |  
 |   ___   |  
 |  ~___~  |  
 | // U \\ |  
 ~_~     ~_~  
 (_________)  
    |___|     
  __[   ]__   
_/         \__
"""

    merchant_art_neutral = r"""
     ___      
  __[___]__   
 (  _   _  )  
 |  0   0  |  
 |         |  
 |    C    |  
 |   ___   |  
 |  ~___~  |  
 | // ○ \\ |  
 ~_~     ~_~  
 (_________)  
    |___|     
  __[   ]__   
_/         \__
"""

    merchant_art_bad = r"""
     ___      
  __[___]__   
 (  \   /  )  
 |  0   0  |  
 |         |  
 |    C    |  
 |   ___   |  
 |  ~___~  |  
 | // _ \\ |  
 ~_~     ~_~  
 (_________)  
    |___|     
  __[   ]__   
_/         \__
"""

    lila_art_good = r"""
       ---______---    
     (  ))~~~~~~   ))  
    (   ) -    - (  )) 
  (   )) (o)---(o)(   )
 (    )      >   (    )
 (   )(      u   (    )
 (__ ) (_________(   ) 
   (_ )   |    |  (_ ) 
       __[vvvvvv]__    
         )      (      
"""

    lila_art_neutral = r"""
     ---______---    
    (  ))~~~~~~  ))   
   (   ) `     `(  ))  
 (   )) (o)---(o)(   ) 
(    )      >   (    ) 
(   )(      -c  (    ) 
(__ ) (_________(   )  
  (_ )   |    |   _    
      __[vvvvvv]__     
        )      (       
"""

    lila_art_bad = r"""
      ---______---     
    (  ))~~~~~~   ))   
   (   ) _     ^(  ))  
 (   )) (o)---(o)(   ) 
(    )      >   (    ) 
(   )(      ^   (    ) 
(__ ) (_________(   )  
  (_ )   |    |  (_ )  
      __[vvvvvv]__     
        )      (       
"""

    finn_art_good = r"""
   ~~~~~~~~~~~   
  ~llll   llll~  
 ~lll_     _lll~ 
|    O     O   | 
|  . .  b  . . | 
 \  .   U   . / 
  \__________/  
     |    |     
 ____~~~~~~____ 
O              O
"""

    finn_art_neutral = r"""
   ~~~~~~~~~~~   
  ~llll   llll~  
 ~lll_     _lll~ 
|    o     o   | 
|  . .  b  . . | 
 \  .   ,   . / 
  \__________/  
     |    |     
 ____~~~~~~____ 
O              O
"""

    finn_art_bad = r"""
   ~~~~~~~~~~~   
  ~llll   llll~  
 ~lll\     /lll~ 
|    O     O   | 
|  . .  b  . . | 
 \  .   ^   . / 
  \__________/  
     |    |     
 ____~~~~~~____ 
O              O
"""

    spirit_art = r"""          
    (_)      (_)          
   (_, \     / ,_)       
     \_{     }_/         
     ~~┼─────┼~~         
       /◌   ◌\           
      (       )          
       \     /           
      _{     }_          
     /         \        
   /│           │\      
  //             \\
 {{ |           | }}
    |     _     │          
    |    / \    |
"""

    wisp_art = r"""
 .---.  
(o   o) 
|     \ 
 \     \
  `^^^^^
"""
    deer_art = r"""
(             )           
 `--(_   _)--'            
      Y-Y                 
     /@@ \                
    /     \               
    `--'.  \             ,
        |   `.__________/)
"""

    raccoon_art = r"""
             .'    `/\_/\
           .'       <@I@>
<((((((((((  )____(  \./
           \( \(   \(\(
            `-"`-"  " "
"""

    fox_art = r"""
   /\   /\   
  //\\_//\\     ____
  \_     _/    /   /
   / * * \    /^^^]
   \_\o/_/    [   ]
    /   \_    [   /
    \     \_  /  /
     [ [ /  \/ _/
    _[ [ \  /_/
"""

    mother_nature_art = r"""
 _,-._   (_/           \_)             
/ \_/ \    `--(_****_)-'              
>-(_)-<   (ccccccccccccc)             
\_/ \_/  (~**~**~**~**~**~)           
  `-'    cc)   =    =   )cc)          
       (ccc|   9    9   |ccc)         
        (c|   ~   )  ~   |c)          
         (c\    ,__    /c)            
            \_       _/       _,-._   
          ____|      |____   / \_/ \  
          /  /        \  \   >-(_)-<  
         /  /\        /\  \  \_/ \_/  
              \      /         `-'    
               \    /                 
"""

    natures_wrath_art = r"""
                                  /                       
    /|      |\          /        _|_                      
 `__\\      //__'     __|_  ____/ ` \                     
    ||     ||      __/    \/ `    `` \  /                 
  \__`\    |'__/ _/ ` `  \  \ \ `  ```\_|_                
    `_\\  //' _ /   __)} | `|  | \  \` `` \               
     /     \__/ ` ) ) )}_/_-/\_/ | . \ . ` \_             
     \ ,  ,  `  ` ) }`}        \_/_\ .\  ``  }_           
     / 6  6    `   /./              \  \  `` .}\      _/)  
    /       _ //  / /                \  \\.  // \  .-(_ (=:
    |      / /  / /                   \ | |  /   \/    \)  
     V^^V</ // / /                     \ | | /            
     ,( </ // /  /                     /  /| /            
     , \, / / \  /                     | | \ /            
        ) \ \  \ \                     |  \ \ \           
*      /   \_|  \_|                     \_|  \_|          

"""