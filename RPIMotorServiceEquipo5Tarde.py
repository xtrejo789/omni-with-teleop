
    def SetState(self, request, context):
        result = rpi_motor_pb2.StateReply()

        try:
            self.v_x = request.vel_x
            self.v_y = request.vel_y
            self.v_yaw = request.vel_yaw
            self.v_heave = request.vel_heave
            self.pitch = request.pitch
            self.leds = request.leds

            theta = np.array([0, 2*np.pi/3, 4*np.pi/3])  # 0°, 120°, 240°
            J = np.array([
                [-np.sin(theta[0]), np.cos(theta[0]), self.R],
                [-np.sin(theta[1]), np.cos(theta[1]), self.R],
                [-np.sin(theta[2]), np.cos(theta[2]), self.R]
            ])

            v = np.array([self.v_x, self.v_y, self.v_yaw])
            self.w = (1/self.r) * np.dot(J, v)

            
            self.new_cmd = True

            result.res = True
        except Exception as e:
            print("ERROR: " + str(e))
            result.res = False

        return result
