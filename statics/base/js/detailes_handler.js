document.addEventListener('DOMContentLoaded', function() {
    function isMobile() {
        return window.innerWidth <= 768; // شما می‌توانید اندازه مورد نظر خود را تنظیم کنید
    }
    
    
    document.querySelectorAll('.description').forEach(description => {
        var charLimit = 0; // تعداد کاراکترهایی که می‌خواهید نمایش داده شوند
        if (isMobile()) {
            charLimit = 150;
            console.log('کاربر از موبایل استفاده می‌کند');
        } else {
            charLimit = 500;
            console.log('کاربر از کامپیوتر استفاده می‌کند');
        }
        const textElement = description.querySelector('.text');
        const fullText = textElement.innerHTML.trim();

        
        console.log(fullText.length)
        if (fullText.length > charLimit) {
            
            const shortText = fullText.substring(0, charLimit) + '...</li></ul>';
            
            textElement.innerHTML = shortText;
            const moreBtn = description.querySelector('.more-btn');
            moreBtn.style.display = 'inline';
            
            moreBtn.addEventListener('click', function() {
                
            console.log('fullText5')
            console.log(fullText)

                if (textElement.innerHTML === shortText) {
                    textElement.innerHTML = fullText;
                    this.innerHTML = 'بستن';
                } else {
                    textElement.innerHTML = shortText;
                    this.innerHTML = 'بیشتر';
                }
            });
        } else {
            description.querySelector('.more-btn').style.display = 'none';
        }
    });
});