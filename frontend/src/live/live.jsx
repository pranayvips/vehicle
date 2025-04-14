import Map from "./map";
import "./live.css"

function LiveTraffic(){
    document.title = "RoadRadar : Live Traffic"

    return (
        <section className="live">
            <Map/>
        </section>
    )
}

export default LiveTraffic;