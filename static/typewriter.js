const typedTextSpan=document.querySelector(".typed-text"),cursorSpan=document.querySelector(".cursor"),textArray=["I love to Code!","I'm a Full-Stack Web Developer!","I'm a Pythonista!","My dream is to work in 'Google'!"],typingDelay=200,erasingDelay=100,newTextDelay=2e3;let textArrayIndex=0,charIndex=0;function type(){charIndex<textArray[textArrayIndex].length?(cursorSpan.classList.contains("typing")||cursorSpan.classList.add("typing"),typedTextSpan.textContent+=textArray[textArrayIndex].charAt(charIndex),charIndex++,setTimeout(type,typingDelay)):(cursorSpan.classList.remove("typing"),setTimeout(erase,newTextDelay))}function erase(){charIndex>0?(cursorSpan.classList.contains("typing")||cursorSpan.classList.add("typing"),typedTextSpan.textContent=textArray[textArrayIndex].substring(0,charIndex-1),charIndex--,setTimeout(erase,erasingDelay)):(cursorSpan.classList.remove("typing"),++textArrayIndex>=textArray.length&&(textArrayIndex=0),setTimeout(type,typingDelay+1100))}document.addEventListener("DOMContentLoaded",function(){textArray.length&&setTimeout(type,newTextDelay+250)});