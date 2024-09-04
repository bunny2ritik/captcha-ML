import React, { useEffect } from 'react';

const CaptureData: React.FC = () => {
    useEffect(() => {
        const browserInfo = {
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            screenWidth: window.screen.width,
            screenHeight: window.screen.height
        };

        const handleMouseMove = (event: MouseEvent) => {
            console.log('Mouse position:', event.clientX, event.clientY);
            fetch('/api/capture-data', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    ...browserInfo,
                    mouseX: event.clientX,
                    mouseY: event.clientY
                })
            });
        };

        document.addEventListener('mousemove', handleMouseMove);

        return () => {
            document.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    return <div>Capturing Data...</div>;
};

export default CaptureData;
