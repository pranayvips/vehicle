import "./home.css";
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import { Pagination } from 'swiper/modules';
import homeVideo from "/src/assets/vid-0.mp4";

const HomeFeature = () => (
  <div className="home-feature">
    <div style={{backgroundColor:"#fff5f5"}}>

    <h1>🔑 Key Features – Content Breakdown</h1>
    <h2>🚦 Adaptive Signal Control</h2>
    <h3>Description:</h3>
    <p>
      Automatically adjusts traffic light durations based on vehicle flow in
      real-time.
      <span>Benefit:</span> Reduces waiting time and optimizes traffic movement.
    </p>
    </div>
    <div style={{backgroundColor:"#fff0f6"}}>

    <h2>📍 Real-Time Traffic Monitoring</h2>
    <h3>Description:</h3>
    <p>
      Live tracking of traffic density using sensors or simulated data,
      displayed on an interactive map.
      <span>Benefit: </span> Helps users and authorities make informed decisions
      quickly.
    </p>
    </div>
    <div style={{backgroundColor:"#f8f0fc"}}>

    <h2>🚓 Emergency Vehicle Priority</h2>
    <h3>Description:</h3>
    <p>
      Detects emergency vehicles (like ambulances or fire trucks) and gives them
      a green corridor.
      <span>Benefit: </span> Reduces response time and clears the way
      automatically.
    </p>
    </div>
    <div style={{backgroundColor:"#f8f9fa"}}>

    <h2>📊 Analytics Dashboard</h2>
    <h3>Description:</h3>
    <p>
      Visual dashboard showing traffic data, congestion heatmaps, signal
      efficiency, and more.
      <span>Benefit: </span> Useful for city planners, traffic police, and
      system admins.
    </p>
    </div>
    <div style={{backgroundColor:"#e3fafc"}}>

    <h2>🧠 AI-Based Congestion Prediction</h2>
    <h3>Description:</h3>
    <p>
      Uses machine learning to predict upcoming congestion based on time, day,
      and historical data.
      <span>Benefit: </span> Prevents traffic jams before they happen.
    </p>
    </div>
    <div style={{backgroundColor:"#f4fce3"}}>

    <h2>🛑 Incident Reporting System</h2>
    <h3>Description:</h3>
    <p>
      Allows users or sensors to report roadblocks, accidents, or unusual
      traffic patterns.
      <span>Benefit: </span> Quick incident response and rerouting.
    </p>
    </div>
    <div style={{backgroundColor:"#e7f5ff"}}>

    <h2>📱 User-Friendly Web Interface</h2>
    <h3>Description:</h3>
    <p>
      Responsive, intuitive interface for users and administrators to monitor
      and interact with the system.
      <span>Benefit: </span> Makes it easy to use on both desktop and mobile.
    </p>
    </div>
    <div style={{backgroundColor:"#fff4e6"}}>

    <h2>🔒 Secure Admin Access</h2>
    <h3>Description:</h3>
    <p>
      Login-based access for admins to control signals, view reports, and manage
      system behavior.
      <span>Benefit: </span> Ensures control remains with authorized personnel.
    </p>
    </div>
  </div>
);

const HomeExample = () =>{
    return (
        <div className="home-example">
            <h1>Original vs. Transformed Output</h1>
            <h2>On the left, you’ll see the original video, and on the right, the transformed version.</h2>
            <div>
                <video src="/src/assets/abc.mp4" muted autoPlay="{true}" loop="{true}"></video>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
  <path strokeLinecap="round" strokeLinejoin="round" d="M7.5 21 3 16.5m0 0L7.5 12M3 16.5h13.5m0-13.5L21 7.5m0 0L16.5 12M21 7.5H7.5" />
</svg>

                <video src="/src/assets/home-example.mp4" muted autoPlay="{true}" loop="{true}"></video>
                <h3>ORIGINAL</h3>
                <h3></h3>
                <h3>TRANSFORMED</h3>
            </div>
        </div>
    )
}

const MakeTestimonial = ({name,feedback}) => {
    return (
        <div className="testimonial">
            <img src={"https://thispersondoesnotexist.com?"+name} alt="" /> 
            <h1>{name}</h1>
            <p>{feedback}</p>
        </div>
    )
}

function Home() {
    document.title = "RoadRadar : Home"
    const testimonials = [
        {
          name: "Ananya Sharma",
          feedback: "This platform exceeded my expectations. The transformation quality is amazing!",
        },
        {
          name: "Ravi Kumar",
          feedback: "Very smooth experience. Loved how fast and clean the results are!",
        },
        {
          name: "Priya Mehta",
          feedback: "Honestly, one of the most intuitive tools I’ve used in a while.",
        },
        {
          name: "Arjun Singh",
          feedback: "I highly recommend this to anyone looking for quick video processing.",
        },
      ];

      
  return (
    <section className="home">
      <div className="home-video">
        <video src={homeVideo} muted autoPlay="{true}" loop="{true}"></video>
        <aside></aside>
        <h1>Smarter Traffic for a Safer City</h1>
        <p>
          Real-time traffic monitoring, smart signal control, and emergency
          response.
        </p>
        <button>
          View Live Map
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth="1.5"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M9 6.75V15m6-6v8.25m.503 3.498 4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 0 0-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0Z"
            />
          </svg>
        </button>
      </div>
      <HomeFeature />
      <HomeExample />
      <div className="reviews">
        <h6>What People Have to Say About Us!!</h6>

      <Swiper
      modules={[Pagination]}
      spaceBetween={20}
      slidesPerView={3}
    //   onSlideChange={() => console.log('slide changed')}
    //   onSwiper={(swiper) => console.log(swiper)}
      pagination={{ clickable: true }}
      loop={true}
      effect="cuberflow" 
      grabCursor={true}
      breakpoints={{
          640: { slidesPerView: 1 },
          768: { slidesPerView: 2 },
          1024: { slidesPerView: 3 },
        }}
        //   or "cube" or "fade"
        >

            {testimonials.map((data,index)=>{
                return <SwiperSlide key={index}><MakeTestimonial name={data.name} feedback={data.feedback} /></SwiperSlide>
            })}
      {/* <SwiperSlide><div style={{ background: '#eee', padding: '2rem' }}>Slide 1</div></SwiperSlide> */}
    </Swiper>
        </div>
    </section>
  );
}

export default Home;
