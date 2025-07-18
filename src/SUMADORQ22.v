module SUMADORQ22(
    input wire clk,
    input wire rst,
    input wire [4:0] a,
    input wire [4:0] b,
    output reg [5:0] c
);
    reg [5:0] a_extended, b_extended, sum_extended;
    reg [4:0] magnitude_a, magnitude_b;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            a_extended <= 0;
            b_extended <= 0;
            sum_extended <= 0;
            magnitude_a <= 0;
            magnitude_b <= 0;
            c <= 0;
        end

        else begin
            

            if(a[3:0] == 0) begin
                c <= {b[4], 1'b0, b[3:0]};
            end

            else if (b[3:0] == 0) begin
                c <= {a[4], 1'b0, a[3:0]};
            end

            else begin
                magnitude_a <= {1'b0, a[3:0]};
                magnitude_b <= {1'b0, b[3:0]};
                a_extended <= a[4] ? -magnitude_a : magnitude_a;
                b_extended <= b[4] ? -magnitude_b : magnitude_b;
                sum_extended <= a_extended + b_extended;       
                if (sum_extended[5]) begin
                    c <= {2'b10, -sum_extended[3:0]};
                end
                else begin
                    c <= {2'b00, sum_extended[3:0]};
                end
            end

        end
    end

endmodule
