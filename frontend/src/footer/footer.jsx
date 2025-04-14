import 'boxicons/css/boxicons.min.css';
import './footer.css'

function Footer(){
    return (
        <footer>
            <h1>Your City. Your Traffic. Smarter.</h1>
            <div className="footer-contact">
                {/* <box-icon type='logo' name='github'></box-icon> */}
                <h2>Contact Us</h2>
                <div><i className='bx bx-map' ></i><a href=""><p>Gurgoan</p></a></div>
                <div><i className='bx bxl-whatsapp' ></i><p>+91 6203241318</p></div>
                <div><i className='bx bxl-gmail' ></i><p>prasadpranay2005@gmail.com</p></div>
                <div className='footer-links'><i className='bx bxl-github' ></i><i className='bx bxl-twitter' ></i><i className='bx bxl-linkedin' ></i><i className='bx bxl-instagram' ></i></div>
            </div>
            <div className="footer-touch" id='contact'>
                <h2>Get in Touch</h2>
                <input type="text" placeholder='Your Name' />
                {/* <input type="email" placeholder='Your Email' required/> */}
                <textarea name="" id="" placeholder='Your Message'></textarea>
                <button>Send Message</button>
            </div>
        </footer>
    )
}
export default Footer;